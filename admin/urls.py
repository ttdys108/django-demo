from django.urls import path
from .views import index, users

app_name = 'admin'
urlpatterns = [
    path('', index.index, name='index'),
    path('users/', users.index, name='users.index'),
    path('users/add', users.add, name='users.add'),
    path('users/update', users.update, name='users.update'),
]