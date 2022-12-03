# -*- encoding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class deposit(models.Model):
    amount = models.CharField(max_length=9999, default=0)
    token = models.CharField(max_length=9999)
    plan = models.CharField(max_length=9999)
    order_id = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return str(self.order_id)


class balance(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       balance = models.IntegerField(default = 0)