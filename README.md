# benranderson.github.io

Personal website built with [Pelican](https://docs.getpelican.com/en/latest/).

Use [uv](https://docs.astral.sh/uv/) for Python dependency management.

## Development

```bash
# Generate the site
make html

# Start development server with auto-reload
make devserver

# Clean generated files
make clean

# Serve the site without auto-reload
make serve
```

## Publishing

The site is automatically updated on each commit via a post-commit hook as described in [this FAQ](https://docs.getpelican.com/en/latest/tips.html#update-your-site-on-each-commit).
