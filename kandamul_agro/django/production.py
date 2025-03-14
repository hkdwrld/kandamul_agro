from .base import *
from kandamul_agro.env import env

DEBUG = env.bool('DJANGO_DEBUG', default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])