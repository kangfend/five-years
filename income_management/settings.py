import os
import socket

PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(PROJECT_DIR)

SECRET_KEY = '(y&#ktl0lzu^q+^clnwpl^-0*jm^46$om5trfdso4(ul7e9l%)'

HOSTNAME = socket.gethostname()
PRODUCTION_SERVERS = ['fiveyearsplan.com']

LIVEHOST = HOSTNAME in PRODUCTION_SERVERS

TEMPLATE_DEBUG = DEBUG = not LIVEHOST

if not LIVEHOST:
    MEDIA_URL = '/media/'
    STATIC_URL = '/static/'
    ADMIN_MEDIA_PREFIX = '/static/admin/'
    SITE_ID = 1
else:
    MEDIA_URL = 'http://cdn.' + HOSTNAME + '/ctrack/media/'
    STATIC_URL = 'http://cdn.' + HOSTNAME + '/ctrack/static/'
    ADMIN_MEDIA_PREFIX = 'http://cdn.' + HOSTNAME + '/ctrack/static/admin/'
    SITE_ID = 2

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'five_years/static/'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    # os.path.join(BASE_DIR, 'templates'),
)

ADMINS = (
    ('Benny Christanto', 'benny.christanto@gmail.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    # ---
    'suit',

    # ---
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # ---
    'smart_selects',
    'rosetta',
    'sorl.thumbnail',
    'south',

    # ---
    'five_years',
)

if DEBUG:
    INSTALLED_APPS += ('debug_toolbar',)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'income_management.urls'

WSGI_APPLICATION = 'income_management.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'five_years.db.sqlite3'),
    }
}


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Makassar'
USE_I18N = True
USE_L10N = True
USE_TZ = True

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',  # required by django-suit (~suit)
)

SUIT_CONFIG = {
    'ADMIN_NAME': 'Income Management',
    'LIST_PER_PAGE': 50
}

AUTOLOAD_TEMPLATETAGS = (
    'globaltags.app_tags',
)

LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/login/'
