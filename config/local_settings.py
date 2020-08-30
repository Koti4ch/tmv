from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7lm+j%3duv(z)nd8+v%40y*=g4m$_kq3c!xk^0b^b1+520fwh5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'tmvdb.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     # {
#     #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     # },
#     # {
#     #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     # },
#     # {
#     #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     # },
#     # {
#     #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     # },
# ]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'mails')