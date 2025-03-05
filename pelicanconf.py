AUTHOR = "Ben Randerson"
SITENAME = "Ben Randerson"
SITEURL = ""
EMAIL = "ben.m.randerson@gmail.com"

PATH = "content"

TIMEZONE = "Europe/London"

DEFAULT_LANG = "en"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}.html"
PAGE_PATHS = ["pages"]
DEFAULT_CATEGORY = "blog"
ARTICLE_URL = "{category}/{slug}.html"
ARTICLE_SAVE_AS = "{category}/{slug}.html"
ARTICLE_EXCLUDES = ["html"]
ARTICLE_PATHS = ["posts"]
CATEGORY_URL = "category/{slug}.html"
CATEGORY_SAVE_AS = "category/{slug}.html"
USE_FOLDER_AS_CATEGORY = False
DRAFT_URL = "drafts/{slug}.html"

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
    ("LinkedIn", "https://www.linkedin.com/in/randersonben"),
    ("GitHub", "https://github.com/benranderson"),
)

DEFAULT_PAGINATION = False

# extra paths
STATIC_PATHS = ["images", "pdfs", "pdfs/cv.pdf"]
EXTRA_PATH_METADATA = {"pdfs/cv.pdf": {"path": "cv.pdf"}}

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
                "text": "Documentation",
                "url": "https://benranderson.github.io/demo/",
            },
            {
                "text": "Source Code",
                "url": "https://github.com/benranderson/demo",
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
