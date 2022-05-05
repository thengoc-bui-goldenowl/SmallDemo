from __future__ import absolute_import, unicode_literals
from argparse import Namespace
import os
from celery import Celery
from celery.schedules import crontab
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SmallDemo.settings")
app=Celery('SmallDemo')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'add',
        'schedule': 5.0,
    },
   
}