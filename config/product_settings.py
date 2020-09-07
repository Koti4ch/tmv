from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ld*bz_k9xwy3+c**xb#k2qna48r2(k2ed9wgq3orwgxvut!wyv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'tmvdb.sqlite3',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# SMTP yandex server
DEFAULT_FROM_EMAIL = 'dkt324@yandex.by'
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.yandex.ru"
EMAIL_HOST_USER = "dkt324@yandex.by"
EMAIL_HOST_PASSWORD = "shilov324"
EMAIL_PORT = 587
EMAIL_USE_TLS = True