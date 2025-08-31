from __future__ import absolute_import,unicode_literals
import os
from celery import Celery,shared_task
from django.conf import settings
from celery.schedules import crontab
#settings a default celery program
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tryRedis.settings')

app = Celery('tryRedis')

app.conf.timezone = "Asia/Tashkent"
app.config_from_object('django.conf:settings',namespace='CELERY')

app.autodiscover_tasks()






app.conf.beat_schedule = {
     'add-every-5-seconds': {
        'task': 'vubon',
        'schedule': 5.0,
    },
    'add-every-minute-contrab': {
        'task': 'data_checking',
        'schedule': crontab(minute=1),
    },
}

