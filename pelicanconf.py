AUTHOR = "Aleksey Kuznetsov"
SITENAME = "Aleksey Kuznetsov's website"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/Moscow"

PAGE_PATHS = ["pages"]

THEME = "."

DEFAULT_LANG = "en"
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
PLUGINS = ["i18n_subsites", "jinja2content"]
I18N_GETTEXT_NEWSTYLE = True
I18N_GETTEXT_LOCALEDIR = "trans/"
I18N_GETTEXT_DOMAIN = "messages"
# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    "en": {"SITENAME": "Aleksey Kuznetsov's website", "THEME_STATIC_DIR": "../static"},
    "ru": {"SITENAME": "website Алексея Кузнецова", "THEME_STATIC_DIR": "../static"},
}
TEMPLATES_PATHS = ["templates"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = False
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

JINJA2CONTENT_TEMPLATES = ["*.md"]
# Blogroll
# LINKS = (
# )

# Social widget
SOCIAL = (
    ("vk", "https://vk.com/wind_blow"),
    (
        "github",
        "https://github.com/w1ndblow",
    ),
    ("gitlab", "https://gitlab.com/w1ndblow"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
