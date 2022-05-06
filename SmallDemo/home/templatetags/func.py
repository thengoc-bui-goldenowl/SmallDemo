import requests
from django import template
from django.core.cache import cache
from django.conf import settings
from datetime import datetime, timedelta
register = template.Library()


@register.filter
def mul(value):
    value = int(value)
    return round(value * get_price(), 2)


def get_price():
    price = cache.get("price")
    if not price:
        try:
            a = requests.get(
                'https://api.currencyapi.com/v3/latest?apikey=q9PDoUP4qywGKHM6sb97uN3Iu4CuaIL4r6nKcIdX')
            price = a.json()['data']['VND']['value']
            cache.set("price", price)
            cache.pexpire_at("price", datetime.now() + timedelta(minutes=5))
        except:
            price = 22800.13454
    return price
