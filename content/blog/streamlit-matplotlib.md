title: Rendering Matplotlib plots on load-balanced Streamlit servers
date: 2025-11-23
modified: 2025-11-23
category: blog
tags: streamlit, matplotlib, deployment, load-balancing
slug: streamlit-matplotlib
authors: Ben Randerson

## The Problem

When running Streamlit applications on load-balanced servers with multiple stateless backend containers, matplotlib plots may fail to render.

For example, this code:

```python
import streamlit as st

fig = generate_matplotlib_fig()
st.pyplot(fig)
```

Can produce this less than useful output:

![render-fail]({static}/images/render-fail.png)

This is because matplotlib plots depend on temporary files saved to the filesystem, and requests routed to different containers may not find the image files created by other containers. Each container has its own ephemeral filesystem with no shared storage between them.

## The Fix

This fix converts matplotlib plots to base64-encoded images embedded directly in the HTML instead of saving them as separate files. It ensures that when the server's load balancer routes requests to different backend containers, the image data travels with the page response rather than requiring a separate file lookup that might hit a different container that doesn't have the file.

```python
import base64
from io import BytesIO
import matplotlib.pyplot as plt
import streamlit as st


def fig_to_html(fig, dpi=100):
    """Convert a Matplotlib figure to base64-encoded HTML img tag.

    Necessary to avoid issues with load-balanced production servers where containers
    don't share a filesystem.

    Args:
        fig: Matplotlib figure object
        dpi: Dots per inch for the output image (default 100 for web display)

    Returns:
        HTML img tag with base64-encoded image data
    """
    with BytesIO() as buf:
        fig.savefig(buf, format="png", bbox_inches="tight", dpi=dpi)
        # close figure to free memory
        plt.close(fig)
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode()
    img_data_uri = f"data:image/png;base64,{img_base64}"
    return f'<img src="{img_data_uri}" style="max-width: 100%; height: auto;">'

fig = generate_matplotlib_fig()
st.markdown(fig_to_html(fig), unsafe_allow_html=True)
```

As a bonus, this should make plot rendering faster than the original `st.pyplot()` approach for typical plot sizes.

This is because the image data is embedded directly in the HTML response, requiring only one HTTP request/response cycle. In contrast, `st.pyplot()` saves the plot to a temporary file, sends HTML with an image reference, and then the browser makes a second HTTP request to fetch the image.

By eliminating this round-trip and the filesystem I/O overhead, the base64 approach can deliver a faster user experience, especially on networks with higher latency.

## Alternative Solutions

While the base64 encoding approach above is the most portable solution, there are other ways to solve this problem:

1. **Shared storage**: Configure persistent volumes that all containers can access
2. **Object storage**: Save plots to S3/blob storage and serve them via signed URLs
3. **"Sticky" sessions**: Configure the load balancer to route users to the same container (not recommended as it reduces load balancing effectiveness)

## What Didn't Work

An earlier attempt to fix this involved converting the figure to a bytes buffer and passing that directly to Streamlit's `st.image()`, as shown below.

```python
# this doesn't work as Streamlit still saves images to temp files on disk
def fig_to_buf(fig):
    """Convert a Matplotlib figure to an image bytes buffer."""
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    # close figure to free memory
    plt.close(fig)
    buf.seek(0)
    return buf

fig = generate_matplotlib_fig() 
st.image(fig_to_buf(fig))
```

However, this didn't work as Streamlit still stores the buffer contents to a temporary file on disk before serving it as an image via `st.image()`, and so the original problem remained.
