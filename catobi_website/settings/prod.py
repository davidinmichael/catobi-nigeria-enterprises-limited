from .base import *
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = False

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("DB_name"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': "localhost",
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
