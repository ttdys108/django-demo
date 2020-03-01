from ..utils import redisTemplate as redis
from django.http import HttpResponse


def weather7d(request, code):
    data = redis.hget('weather7d', code)
    decoded = data.decode('unicode_escape') if data else None
    return HttpResponse(decoded, content_type='application/json')

def weather(request, code):
    data = redis.hget('weather_today', code)
    decoded = data.decode('unicode_escape') if data else None
    return HttpResponse(decoded, content_type='application/json')

