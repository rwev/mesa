#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# PELICAN VARIABLES REFERENCED BY TEMPLATE

OWNER = ""
AUTHOR = ""

SITENAME = ""
SITEURL = "localhost:8000"

USER_LOGO_URL = ""
TAGLINE = ""

DISPLAY_LINKS_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_SOCIAL_ON_MENU = False

LINK_ITEMS = (
    # ("<TEXT>", "<URL>"),
)
SOCIAL = ()

# CONFIGURATIONS FOR PELICAN BUILD PROCESS

THEME = "mesa"
RELATIVE_URLS = True

# PLUGINS

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    "autopages",
    "similar_posts",
    "neighbors",
    "more_categories",
    "photos",
    "summary",
    "clean_summary",
]

# autopages
AUTOPAGES_PATH = ""

AUTHOR_PAGE_PATH = ""
CATEGORY_PAGE_PATH = ""
TAG_PAGE_PATH = ""

# similar_posts
SIMILAR_POSTS_MAX_COUNT = 3

# photos
PHOTO_LIBRARY = ""

# 1.33~ width / height ratio
# (width, height, quality % of max)
PHOTO_GALLERY = (2000, 1500, 95)
PHOTO_ARTICLE = (760, 506, 95)
PHOTO_THUMB = (300, 225, 70)

PHOTO_SQUARE_THUMB = True
PHOTO_RESIZE_JOBS = 5
PHOTO_WATERMARK = False

PHOTO_EXIF_KEEP = False
PHOTO_EXIF_REMOVE_GPS = True

PHOTO_EXIF_COPYRIGHT = "CC-BY-NC-ND"
PHOTO_EXIF_COPYRIGHT_AUTHOR = ""

# summary
SUMMARY_MAX_LENGTH = 1000  # use whole summary
SUMMARY_USE_FIRST_PARAGRAPH = True

CLEAR_SUMMARY_MAXIMUM = 0
CLEAN_SUMMARY_MINIMUM_ONE = False

# CONFIGURATIONS FOR MESA STATIC APPEARANCE (NOT USED BY PELICAN)

MESA_SEPARATION_STR = " // "

MESA_BLOG = "blog"
MESA_LINKS = "links"
MESA_SOCIAL = "social"

MESA_HOME = "home"
MESA_ARCHIVES = "archives"
MESA_SIMILAR_ARTICLES = "similar articles"

MESA_PAGES = "pages"

MESA_AUTHOR = "author"
MESA_AUTHORS = "authors"
MESA_AUTHOR_S = "author(s)"

MESA_CATEGORY = "category"
MESA_CATEGORIES = "categories"

MESA_ARTICLES = "articles"

MESA_GALLERY = "gallery"

MESA_TAG = "tag"
MESA_TAGS = "tags"

MESA_PREVIOUS = "prev"
MESA_NEXT = "next"

MESA_NEWER = "newer"
MESA_OLDER = "older"

MESA_POSTED = "posted"
MESA_MODIFIED = "modified"

MESA_ATOM = "atom"
MESA_RSS = "rss"

# FORMATTING / FEED GENERATION

DEFAULT_DATE_FORMAT = "%Y.%m.%d %H:%M"  # big

TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

AUTHOR_FEED_ATOM = "feeds/author.{slug}.atom.xml"
AUTHOR_FEED_RSS = "feeds/author.{slug}.rss.xml"

TAG_FEED_ATOM = "feeds/tag.{slug}.atom.xml"
TAG_FEED_RSS = "feeds/tag.{slug}.rss.xml"

CATEGORY_FEED_ATOM = "feeds/category.{slug}.atom.xml"
CATEGORY_FEED_RSS = "feeds/category.{slug}.rss.xml"

FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS =  "feeds/all.rss.xml"
