"""
Django settings for unitywebapp project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!




# DEBUG = True
# ALLOWED_HOSTS = []

DEBUG = False
ALLOWED_HOSTS = ['unitycenter.pythonanywhere.com','unityctr.org','www.unityctr.org', '127.0.0.1']



# Application definition

INSTALLED_APPS = [
    'sendemail.apps.SendemailConfig',
    'users.apps.UsersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'newsletters',
    'gallery',
    'pages',
    'blogs',
    'pdfform',
    'crispy_forms',
    'django_cleanup.apps.CleanupConfig',
    'hitcount',
    'tinymce',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'unitywebapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'newsletters.custom_context_processor.blog_post_latest',
            ],
        },
    },
]

WSGI_APPLICATION = 'unitywebapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]





# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DJANGORESIZED_DEFAULT_SIZE = [1920, 1080]
DJANGORESIZED_DEFAULT_QUALITY = 75
DJANGORESIZED_DEFAULT_KEEP_META = True
DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'JPEG'
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'JPEG': ".jpg"}
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT =os.path.join(BASE_DIR, 'media')
MEDIA_URL ='/media/'
CRISPY_TEMPLATE_PACK ='bootstrap4'

LOGIN_REDIRECT_URL = 'unity-index'
LOGIN_URL = 'login'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
VENV_PATH = os.path.dirname(BASE_DIR)
STATIC_ROOT = os.path.join(VENV_PATH, 'static')


#MEDIA_ROOT = os.path.join(VENV_PATH, 'media_root')


EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')


MAILCHIMP_API_KEY= env('MAILCHIMP_API_KEY')
MAILCHIMP_DATA_CENTER=env('MAILCHIMP_DATA_CENTER')
MAILCHIMP_EMAIL_LIST_ID =env('MAILCHIMP_EMAIL_LIST_ID')




# TINYMCE_JS_URL = os.path.join(STATIC_URL, 'tinymce/js/tinymce/tinymce.min.js')
# TINYMCE_DEFAULT_CONFIG = {
#     'plugins': "table,spellchecker,paste,searchreplace,image,imagetools,media,codesample,link,code",
#     'theme': "silver",
#     'cleanup_on_startup': True,
#     'content_css': 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css',
#     'custom_undo_redo_levels': 10,
#     'menubar': True,
#     'statusbar': True,
#     'height': 500,
#     'toolbar_mode': 'wrap' ,
#     'toolbar': 'undo redo | styleselect | bold italic | link | alignleft aligncenter alignright | link image',
#     'extended_valid_elements': 'i[*],img[*]',

# }
TINYMCE_DEFAULT_CONFIG  = {
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': 'link image preview codesample contextmenu table code',
    'toolbar1': 'bold italic underline | alignleft aligncenter alignright alignjustify '
               '| bullist numlist | outdent indent | table | link image | codesample | preview code',
    'contextmenu': 'formats | link image',
    'content_css': 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css',
    'menubar': True,
    'toolbar_mode': 'wrap' ,
    'inline': False,
    'statusbar': True,
    'height': 360,
    'width':900,
}


TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = False
