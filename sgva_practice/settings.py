import os
from pathlib import Path

# Construye las rutas dentro del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURIDAD: Mantén esta clave en secreto en producción
SECRET_KEY = 'django-insecure-tu-clave-aqui'

DEBUG = True  # Cambiar a False cuando despliegues en Render

ALLOWED_HOSTS = ['*'] # Permite que Codespaces y Render lo visualicen

# Registro de Aplicaciones
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Tu aplicación
    'gestion_empresas',
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

ROOT_URLCONF = 'sgva_practice.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Indicamos a Django que busque en tu carpeta 'templates' de la raíz
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

WSGI_APPLICATION = 'sgva_practice.wsgi.application'

# Base de Datos

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sgva_practice_db',
        'USER': 'root',
        'PASSWORD': 'admin123', 
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Internacionalización
LANGUAGE_CODE = 'es-co' # Español de Colombia
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

# Archivos Estáticos (CSS, JavaScript, Imágenes)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'