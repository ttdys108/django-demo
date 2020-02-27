from django.http import HttpResponse, HttpResponseForbidden
from django.core.cache import cache
import re
from ..utils import Redis
import string
import json


class AuthMiddleware:
    public_path = ['/admin/login/', '/admin/register/', '/admin/']

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path in AuthMiddleware.public_path:
            return self.get_response(request)
        try:
            token = re.sub('Bearer\s*', '', request.headers['Authorization'])
        except KeyError:
            print('token is required for request: ', request.path)
            return HttpResponse(status=401)
        # validate token
        auth = Redis.get('_token:' + token)
        if not auth:
            print('token: ', token, ' has expired!')
            return HttpResponse(status=401)
        jsonauth = json.loads(auth)
        print('uid: ', jsonauth['uid'])
        return self.get_response(request)
