"""
Django settings for dataduck project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__name__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tweet_collector',
    'emberduck',
    'users',
    'pipeline',
    'tastypie'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dataduck.urls'

WSGI_APPLICATION = 'dataduck.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TEMPLATE_DIRS = {
    os.path.join(PROJECT_ROOT, 'templates'),
    os.path.join(PROJECT_ROOT, 'users/templates')
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

print(os.path.join(PROJECT_ROOT, 'static'))

STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    ('assets', os.path.join(PROJECT_ROOT, 'static')),
    ('assets', os.path.join(PROJECT_ROOT, 'emberduck/static')),
)

# STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# PIPELINE_CSS = {
#     'application': {
#         'source_filenames': (
#           'css/emberduck.css',
#         ),
#         'output_filename': 'css/application.css',
#     },
# }

# PIPELINE_JS = {
#    'application': {
#         'source_filenames': (
#             'js/templates/**/*.js'
#         ),
#         'output_filename': 'js/application.js'
#    }
# }
