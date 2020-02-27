from django.shortcuts import render
from django.http import HttpResponse, Http404
from ..models import User
from django.utils import timezone
import json


def index(request):
    return HttpResponse('user index')


def add(request):
    user = User(username='django', password='123456')
    user.save()
    print('save succeed! user: ', user.id)
    resp = {'code': '000000', 'msg': 'success'}
    return HttpResponse(json.dumps(resp), content_type='application/json')

def update(request):
    params = json.loads(request.body.decode())
    user = User.objects.get(pk=params.get('userId'))
    user.mobile = '18627219552'
    user.save()
    resp = {'code': '000000', 'msg': 'success'}
    return HttpResponse(json.dumps(resp), content_type='application/json')
