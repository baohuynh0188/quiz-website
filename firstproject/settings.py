"""
Django settings for firstproject project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#%!qb%&h1^#nsh0gfmtju&^7n414-a88to)nfy#zc89$45j0!0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    #Thêm app vào setting (QuizConfig và UsersConfig là tên của class trong apps.py của mỗi app)
    'quiz.apps.QuizConfig',
    'users.apps.UsersConfig',
    'docum.apps.DocumConfig',
    'home.apps.HomeConfig',
    'search.apps.SearchConfig',
    'phonenumber_field',
    'rest_framework',
    'crispy_forms',
    'nested_admin',
    'tinymce',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'firstproject.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'firstproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hushare',
        'USER': 'root',
        'PASSWORD': '0188',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': { 'init_command': 'SET storage_engine=INNODB' }
    },
    'postgresql': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hushare',
        'USER': 'postgres',
        'PASSWORD': '0188',
        'HOST': '127.0.0.1',
        'PORT': '5432',
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

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'vi-VI'

TIME_ZONE = 'Asia/Ho_Chi_Minh'

# DATE_INPUT_FORMATS = ('%d-%m-%Y')

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
   os.path.join(BASE_DIR, 'locale'),
)

LANGUAGES = (
    ('vi', _('Vietnamese')),
    ('en', _('English')),
)

MULTILINGUAL_LANGUAGES = (
    "en-us",
    "vi",
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

#Dùng để chỉ url cho thư mục static
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#Dùng để hướng url lưu ảnh mà người dùng upload lên
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#Dùng để sử dụng Crispy template cho form nhập
CRISPY_TEMPLATE_PACK = 'bootstrap4'

#Khi login thì sẽ chuyển đến trang chủ
LOGIN_REDIRECT_URL = 'home'
#Khi người dùng vào trang profile/ thì sẽ hiện trang đăng nhập trước rồi sau đó mới vào trang profile
LOGIN_URL = 'login'

# Password Reset Sever
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_POST = 587
EMAIL_USE_TLS = True
# Tài khoản và mật khẩu email
#EMAIL_HOST_USER = 'caube.caro.lokckok@gmail.com'
#EMAIL_HOST_PASSWORD = 'duujxvpgzgisxlvu'
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')

GOOGLE_RECAPTCHA_SECRET_KEY = '6LcJ_OQUAAAAAMWLGwZn-f5Q83wsXvog2EnqR5_b'

TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 1120,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    }

SITE_ID = 1
