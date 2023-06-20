import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fresh_food.settings')

app = Celery('fresh_food')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()