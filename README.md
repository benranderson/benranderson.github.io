# benranderson.github.io

Personal website built with [Pelican](https://docs.getpelican.com/en/latest/).

Use [uv](https://docs.astral.sh/uv/) for Python dependency management.

## Development

```bash
# Generate the site
make html

# Start development server with auto-reload (recommended)
make devserver

# Clean generated files
make clean

# Serve the site without auto-reload
make serve
```

## Publishing

Generate production site and publish to GitHub Pages.

```bash
# Build with production settings
make publish
# Deploy to GitHub Pages
make github
```