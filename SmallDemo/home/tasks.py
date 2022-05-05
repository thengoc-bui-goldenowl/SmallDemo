from __future__ import absolute_import, unicode_literals
from unicodedata import name
from celery import shared_task
from celery import Celery
import random
@shared_task(name="add")
def add():
    mylist = ["apple", "banana", "cherry"]
    return random.choice(mylist)

# a=requests.get('https://api.currencyapi.com/v3/latest?apikey=q9PDoUP4qywGKHM6sb97uN3Iu4CuaIL4r6nKcIdX')
# print(a.json()['data']['USD'])