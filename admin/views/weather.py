from ..utils import redisTemplate as redis
from django.http import HttpResponse


def weather7d(request, code):
    res = redis.hget('weather7d', code).decode('unicode_escape')
    return HttpResponse(res, content_type='application/json')

