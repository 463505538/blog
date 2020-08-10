import os

from .base import *  # NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': 'wj522059',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

