from __future__ import absolute_import,unicode_literals
import os
from celery import Celery,shared_task
from django.conf import settings
from celery.schedules import crontab
#settings a default celery program
os.environ.setdefault('DJANGO_SETTINGS_MODULE','celery')

app = Celery('celeryapp',
             broker='redis://127.0.0.1:6379/0',
             backend='redis://127.0.0.1:6379/0')

app.conf.timezone = "Asia/Tashkent"
app.config_from_object('django.conf:settings',namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    import time
    x =2
    y=3
    i=0
    while i<5:
        time.sleep(1)
        print("Processing..")
        i+=1
    return x**2+y**2

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

