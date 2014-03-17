#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals


SITENAME = u'Engineering Notebook'
AUTHOR = u'Devin R. Berg'
TAGLINE = u'Not a blog. A notebook to collect my thoughts in.'
SITEURL = 'http://localhost:8000'
FEED_DOMAIN = SITEURL
#FEED_ATOM = 'feeds/all.atom.xml'
FEED_RSS = 'feeds/all.rss'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = u'en'
DATE_FORMATS = {
    'en': '%Y/%m/%d',
}
DEFAULT_PAGINATION = 5

THEME = 'themes/tuxlite_tbs'


# display items
LOGO_URL = 'http://www.devinandlauren.com/images/flower_single_sm.png'
MENUITEMS = (
    ('archives', '/archives.html'),
    ('profile', 'http://www.uwstout.edu/faculty/bergdev'),
    ('home', 'http://www.devinberg.com'),
)
DISPLAY_PAGES_ON_MENU = True
FOOTER_MESSAGE = u'This work is licensed under the <a href="http://creativecommons.org/licenses/by/4.0/" rel="license">CC BY</a>.'
TWITTER_USERNAME = u'devinberg'
DISQUS_SITENAME = u'devinsnotebook'

PATH = "content"

STATIC_PATHS = ['images',
    'extra/README',
    'extra/LICENSE',
    'extra/CNAME',
    'extra/humans.txt',
    'extra/favicon.ico',
    '404.md',
    'code',
    ]
EXTRA_PATH_METADATA = {
    'extra/README': {'path': 'README'},
    'extra/LICENSE': {'path': 'LICENSE'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/humans.txt': {'path': 'humans.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    '404.md': {'path': '404.md'},
}
TYPOGRIFY = True

# Plugins and their settings.
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ('sitemap',
    'render_math',
    'liquid_tags.img',
    'liquid_tags.youtube',
    'liquid_tags.include_code',
    )

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'weekly',
        'pages': 'monthly'
    }
}
