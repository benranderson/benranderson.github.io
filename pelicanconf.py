AUTHOR = "Ben Randerson"
SITENAME = "Ben Randerson"
SITEURL = ""
EMAIL = "ben.m.randerson@gmail.com"

PATH = "content"

TIMEZONE = "Europe/London"

DEFAULT_LANG = "en"

# Theme
THEME = "theme"

# MARKDOWN
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {
            "noclasses": False,
        },
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.fenced_code": {},
    },
    "output_format": "html5",
}

# Content organization
ARTICLE_PATHS = ["blog", "projects"]
PAGE_PATHS = [""]
PAGE_EXCLUDES = ["blog", "projects"]

# URL structure
ARTICLE_URL = "{category}/{slug}.html"
ARTICLE_SAVE_AS = "{category}/{slug}.html"
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"

# Custom page for projects listing
DIRECT_TEMPLATES = ["index", "tags", "categories", "archives"]
TEMPLATE_PAGES = {"projects.html": "projects.html"}

# Static files
STATIC_PATHS = ["images", "cv.pdf", "favicon.svg"]
EXTRA_PATH_METADATA = {
    "cv.pdf": {"path": "cv.pdf"},
    "favicon.svg": {"path": "favicon.svg"},
}

# Copy JS files
THEME_STATIC_PATHS = ["static"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("Email", f"mailto:{EMAIL}"),
    ("LinkedIn", "https://linkedin.com/in/ben-randerson"),
    ("GitHub", "https://github.com/benranderson"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PROJECTS = [
    {
        "text": "Cookiecutter PyPackage: Cookiecutter template for a Python package",
        "links": [
            {
                "text": "Source Code",
                "url": "https://github.com/benranderson/cookiecutter-pypackage",
            },
        ],
    },
    {
        "text": "demo: Demonstration Python Application",
        "links": [
            {
                "text": "Source Code",
                "url": "https://github.com/benranderson/demo",
            },
            {
                "text": "Documentation",
                "url": "https://benranderson.github.io/demo/",
            },
        ],
    },
    {
        "text": "composite-pipe: Extract axial, bending and torsional stiffnesses for composite pipe, based on material and layup properties",
        "links": [
            {
                "text": "Source Code",
                "url": "https://github.com/benranderson/composite-pipe",
            },
        ],
    },
    {
        "text": "UsefulFuncs: Useful VBA functions",
        "links": [
            {
                "text": "Source Code",
                "url": "https://github.com/benranderson/UsefulFuncs",
            },
        ],
    },
]
