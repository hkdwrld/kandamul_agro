from kandamul_agro.env import env

CELERY_BROKER_URL = env('CELERY_BROKER_URL')

#Let's imagine we're using "django-celery-results" extension for storing
#Task results in DB
CELERY_RESULT_BACKEND = "django-db"
CELERY_RESULT_EXTENDED = True