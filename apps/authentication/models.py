# -*- encoding: utf-8 -*-


from django.db import models
import uuid

# Create your models here.
class deposit(models.Model):
    amount = models.CharField(max_length=9999, default=299)
    token = models.CharField(max_length=9999, default="BTC")
    plan = models.CharField(max_length=9999, default="S")
    order_id = models.UUIDField(default=uuid.uuid4, null=False, auto_created=True)

    def __str__(self):
        return str(self.order_id)

class variables(models.Model):
    USDT = models.CharField(max_length=9999, null=False, default="usdt_address")
    BTC = models.CharField(max_length=9999, null=False, default="btc_address")
    ETH = models.CharField(max_length=9999, null=False, default="eth_address")

class others(models.Model):
    total_orders = models.IntegerField(default=6248, null=False)
    revenue = models.IntegerField(default=431594, null=False)