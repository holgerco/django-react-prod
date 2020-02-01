import os
from .installed_apps import INSTALLED_APPS
from .middleware import MIDDLEWARE
from .templates import TEMPLATES
from .databases import DATABASES
from .auth import AUTH_USER_MODEL, AUTH_PASSWORD_VALIDATORS, SECRET_KEY
from .localization import LANGUAGE_CODE, TIME_ZONE, USE_I18N, USE_L10N, USE_TZ
from .urls import ROOT_URLCONF
from .static import STATIC_ROOT, MEDIA_ROOT, MEDIA_URL, STATIC_URL, STATICFILES_DIRS
from .server import ALLOWED_HOSTS, DEBUG, WSGI_APPLICATION
