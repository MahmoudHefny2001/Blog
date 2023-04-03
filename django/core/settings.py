from pathlib import Path

import os

import dj_database_url

from dotenv import load_dotenv

load_dotenv('.env')

from datetime import timedelta

from django.conf import settings

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-$2xwsccsiye9q&xxow6ghoetgw+eo)611+q$%6psabily0i8mm'
# SECRET_KEY = os.environ.get('SECRET_KEY', None)

DEBUG = True
# DEBUG = bool(os.environ.get('DEBUG', None))

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['yourdomain.com', '127.0.0.1']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "corsheaders", #

    "whitenoise.runserver_nostatic",  #

    "storages",

    'django_filters',   #

    'rest_framework',  #
    'rest_framework_simplejwt', #
    'rest_framework_simplejwt.token_blacklist', #

    'uritemplate',  #
    'coreapi',  #

    'blog', #
    'blog_api', #
    'users', #
]

AUTH_USER_MODEL = 'users.NewUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    "whitenoise.middleware.WhiteNoiseMiddleware",   #

    'django.contrib.sessions.middleware.SessionMiddleware',

    "corsheaders.middleware.CorsMiddleware",    #

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'

# render postgres db connection
#DATABASES = {
#    'default': dj_database_url.parse(os.environ.get('DATABASE_URL')),
#}

# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
    # }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # 'DATABASE_URL': os.environ.get('DATABASE_URL'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
        # 'TEST': {
        #     'NAME': '',
        # },
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # 
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAdminUser',
        'rest_framework.permissions.AllowAny',
    ],

    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),

    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],

    'TEST_REQUEST_DEFAULT_FORMAT': 'json',

    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    
}

CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000/api/admin/create/',
    'https://hefnyspace.onrender.com',
    "https://hefnyspace.ninja",
    "https://hefny-blog.up.railway.app"
]

CORS_ALLOWED_ORIGINS = [
    "https://hefnyspace.ninja",
    "http://hefnyspace.ninja",

    "https://hefnyspace.netlify.app",

    "http://localhost:3000",
    "http://127.0.0.1:3000",

    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:8080",
    "http://192.168.0.222:8080",
    
    "https://hefny-space.onrender.com",
    
]

CORS_ALLOW_HEADERS = "access-control-allow-origin"

CORS_ORIGIN_WHITELIST = [
    "https://hefnyspace.ninja",
    "https://hefnyspace.ninja/login",
    "http://hefnyspace.ninja",

    "https://hefnyspace.netlify.app",

    "http://localhost:3000",
    "http://127.0.0.1:3000",

    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8000/api/",
    "http://localhost:8080",
    "http://192.168.0.222:8080",
    
    "https://hefny-space.onrender.com",
    "https://hefnyspace.ninja/",
    "http://hefnyspace.ninja/"

    "http://127.0.0.1:8000/admin/",
]

CORS_ALLOW_HEADERS = "access-control-allow-origin"

# SESSION_COOKIE_SAMESITE = "None"
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True   

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=10),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': settings.SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('JWT',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join('BASE_DIR', 'staticfiles')



# STORAGES = {"default": "storages.backends.s3boto3.S3Boto3Storage"}
# STORAGES = {"staticfiles": "storages.backends.s3boto3.S3StaticStorage"}
# STORAGES = {"staticfiles": "storages.backends.s3boto3.S3ManifestStaticStorage"}


# AWS_ACCESS_KEY_ID = 'AKIA2JMJJU47X5DTB6W4'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'zeet-tf-5422bf57-41a9-40c3-8852-bb43b72ed569'
# AWS_S3_REGION_NAME = "us-west-2"
# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = None
# AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# AWS_DEFAULT_ACL = 'public-read'

# AWS_LOCATION = 'static'

# # s3 static settings
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# # 
# # s3 public media settings
# # PUBLIC_MEDIA_LOCATION = 'media'
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
 
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

