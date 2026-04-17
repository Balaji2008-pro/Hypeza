from pathlib import Path
from datetime import timedelta
import os

# -------------------------
# BASE
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "your-secret-key"

DEBUG = True

ALLOWED_HOSTS = ["*"]

# -------------------------
# APPLICATIONS
# -------------------------
INSTALLED_APPS = [
    # Django default
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third party
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    "channels",

    # Your app
    "api",
]

# -------------------------
# CUSTOM USER MODEL
# -------------------------
AUTH_USER_MODEL = "api.User"

# -------------------------
# MIDDLEWARE
# -------------------------
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# -------------------------
# ROOT URL
# -------------------------
ROOT_URLCONF = "mysproject.urls"

# -------------------------
# WSGI & ASGI
# -------------------------
WSGI_APPLICATION = "mysproject.wsgi.application"
ASGI_APPLICATION = "mysproject.asgi.application"

# -------------------------
# DATABASE (MySQL)
# -------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "bablue",
        "USER": "root",
        "PASSWORD": "Fuck321",
        "HOST": "localhost",
        "PORT": "3306",
    }
}

# -------------------------
# CHANNELS (Redis)
# -------------------------
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

# -------------------------
# TEMPLATES
# -------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# -------------------------
# REST FRAMEWORK + JWT
# -------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# -------------------------
# CORS
# -------------------------
CORS_ALLOW_ALL_ORIGINS = True

# -------------------------
# STATIC & MEDIA
# -------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# -------------------------
# DEFAULT AUTO FIELD
# -------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"