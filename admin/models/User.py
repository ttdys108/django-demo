from django.db import models


class User(models.Model):
    class Meta:
        db_table = 'tbl_user'
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, null=True)
    password = models.CharField(max_length=64, null=True)
    account = models.CharField(max_length=32, null=True)
    avatar = models.CharField(max_length=128, null=True)
    nickname = models.CharField(max_length=64, null=True)
    mobile = models.CharField(max_length=16, null=True)
    email = models.CharField(max_length=128, null=True)
    status = models.CharField(max_length=10, default='NEW')
    device_id = models.CharField(max_length=128, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


