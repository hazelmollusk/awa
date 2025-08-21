from glob import glob
from pathlib import Path
from awa.util import AwaConfig

# from filebrowser.sites import site

BASE_DIR = Path(__file__).resolve().parent.parent

config = AwaConfig(root=BASE_DIR)
for k, v in config.constants.items():
    locals()[k] = v

custom_apps = config.apps or []
INSTALLED_APPS = [
    # admin extensions (needs to be before admin)
    "admin_interface",
    "colorfield",
    "storages",
    # "tinymce",
    # "sorl.thumbnail",
    # "mce_filebrowser",
    # "django_quill",
    # "ckeditor",
    # "markdownx",
    # "grappelli",
    # "filebrowser",
    # "djangocms_text",
    # needed fror admin interface
    "fontawesomefree",
    "django_summernote",
    # django defaults
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party django apps
    "nested_admin",
    "django_extensions",
    "guardian",
    "rest_framework",
    "social_django",
    "sortedm2m",
    "simple_history",
    # awa modules
    "apps.people",
    "awa",
    "apps.pages",
    "apps.posts",
    "apps.tags",
] + custom_apps

# SITE_ID = config.site_id or 1
WSGI_APPLICATION = "awa.wsgi.application"

scheme = "http" if not config.https else "https"
DEBUG = config.debug or False

DOMAINS = []
for p in config.projects:
    for d in p.domains:
        DOMAINS.append(d.domain)

# ALLOWED_HOSTS = DOMAINS
ALLOWED_HOSTS = ["*"]  # for ELB/CF/etc
CSRF_TRUSTED_ORIGINS = [f"{scheme}://{d}" for d in DOMAINS]
# CSRF_COOKIE_DOMAIN = DOMAINS[0]
CORS_ORIGIN_WHITELIST = CSRF_TRUSTED_ORIGINS
if DEBUG:
    CORS_ORIGIN_ALLOW_ALL = True


DATABASES = config.databases.to_dict() or {}
SECRET_KEY = config.secret_key or "aWaSecRet"
X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]
CSRF_USE_SESSIONS = True

AUTH_USER_MODEL = "people.Person"
GUARDIAN_MONKEY_PATCH_USER = False
# GUARDIAN_MONKEY_PATCH = False
# GUARDIAN_USER_OBJ_PERMS_MODEL = 'mana.UserPermission'
# GUARDIAN_GROUP_OBJ_PERMS_MODELS = 'mana.GroupPermission'
# ANONYMOUS_USER_ID = -1
# ANONYMOUS_USER_NAME = 'nobody'
# GUARDIAN_GET_INIT_ANONYMOUS_USER = 'apps.mana.models.get_anonymous_user'
# GUARDIAN_RENDER_403 = True
# GUARDIAN_TEMPLATE_403 =

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ]
}

TEMPLATE_CONTEXT_PROCESSORS = []
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django_currentuser.middleware.ThreadLocalUserMiddleware",
]

ROOT_URLCONF = "awa.urls"

# TEMPLATE_DIR = BASE_DIR / 'templates'
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # FIXME to support multiple host/projects
        # "DIRS": [BASE_DIR / "sites|avatars" / f"{xxxxx}" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
                "awa.context_processors.awa",
            ],
        },
    },
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}

MEDIA_URL = "media/"
# MEDIA_URL = config.storages.default.base_url or "media/"
# MEDIA_ROOT = f"{BASE_DIR}/.media"
# STATIC_URL = config.storages.staticfiles.base_url or "static/"
# STATIC_ROOT = f"{BASE_DIR}/.static"
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

NODE_STATIC_GLOB = BASE_DIR / "node_modules" / "*" / "dist"
STATICFILES_DIRS = glob(NODE_STATIC_GLOB.as_posix())

STATIC_URL = config.storages.staticfiles.OPTIONS.location or "static/"
MEDIA_URL = config.storages.default.OPTIONS.location or "media/"

AWS_ACCESS_KEY_ID = config.connections.aws.key
AWS_SECRET_ACCESS_KEY = config.connections.aws.secret

from django_summernote.settings import ATTRIBUTES

ATTRIBUTES["img"] = ["src", "height", "width", "style", "class"]
SUMMERNOTE_CONFIG = {
    "iframe": True,
    "summernote": {
        "toolbar": [
            ["style", ["style"]],
            ["font", ["bold", "underline", "strikethrough", "clear"]],
            # ['fontname', ['fontname']],
            # ['color', ['color']],
            ["para", ["ul", "ol", "paragraph"]],
            # ['table', ['table']],
            ["insert", ["link", "picture", "video"]],
            # ['view', ['fullscreen', 'codeview', 'help']],
        ],
        # "toolbar":{
        #     ('style', ('style',),),
        #     ('font', ('bold', 'underline', 'clear')),
        #     ('para', ('ul', 'ol', 'paragraph')),
        # }
        "width": "600px",
        "height": "300px",
    },
}

PASSWORD_VALIDATION = "django.contrib.auth.password_validation"
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": f"{PASSWORD_VALIDATION}.UserAttributeSimilarityValidator",
    },
    {
        "NAME": f"{PASSWORD_VALIDATION}.MinimumLengthValidator",
    },
    {
        "NAME": f"{PASSWORD_VALIDATION}.CommonPasswordValidator",
    },
    {
        "NAME": f"{PASSWORD_VALIDATION}.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/New_York"
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# #### social_django #######
# TODO: add backends dynamically based on config
AUTHENTICATION_BACKENDS = [
    "social_core.backends.facebook.FacebookOAuth2",
    "social_core.backends.github.GithubOAuth2",
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.twitter.TwitterOAuth",
    "django.contrib.auth.backends.ModelBackend",
    "guardian.backends.ObjectPermissionBackend",
    "apps.people.backends.AwaBackend",
]
LOGIN_URL = "awa:login"
LOGIN_REDIRECT_URL = "index"  # FIXME: "awa:index"
LOGOUT_URL = "awa:logout"
LOGOUT_REDIRECT_URL = "index"  # noqa: F405
# for extra info
SOCIAL_AUTH_FACEBOOK_SCOPE = [
    "email",
]
SOCIAL_AUTH_JSONFIELD_ENABLED = True
SOCIAL_AUTH_URL_NAMESPACE = "social"
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
SOCIAL_AUTH_LOGIN_REDIRECT_URL = "index"

SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.social_user",
    "social_core.pipeline.user.get_username",
    "social_core.pipeline.social_auth.associate_by_email",
    "social_core.pipeline.user.create_user",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
    "social_core.pipeline.user.user_details",
)

# ######### awa ##################
try:
    from config.local_settings import *  # noqa
except ImportError:
    pass
