import os
import django
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'udm.settings')
django.setup()


app = Celery('udm')

app.config_from_object('django.conf:settings', namespace="CELERY")

app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)
