import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True 

if DEBUG == True:

    SECRET_KEY = '!8z7%#88q0b_saphy285e2b&lms#5xvor%hy=ycv4fb$9tt^vi'


    ALLOWED_HOSTS = []

    SESSION_COOKIE_AGE = 86400
    CART_SESSION_ID = 'cart'


    LOGIN_URL = 'login'
    LOGIN_REDIRECT_URL = 'cart-detail'
    LOGOUT_REDIRECT_URL = 'hjemme'

    INSTALLED_APPS = [
        'django.contrib.sites',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sitemaps',
        'apps.core',
        'apps.order',
        'apps.store',
        'apps.blog',
        'apps.cart',
        'apps.userprofile',
        'apps.newsletter', 
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

    ROOT_URLCONF = 'demo.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['C:/Users/Home/Desktop/websites/personal/shop/core/templates'],
            'APP_DIRS' : True,
            'OPTIONS' : {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'apps.cart.context_processors.cart',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'demo.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/3.1/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


    # Password validation
    # https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/3.1/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.1/howto/static-files/

    STATIC_URL = 'static/'
    STATICFILES_DIRS = [
        BASE_DIR / "static"
    ]
    MEDIA_URL='images/'