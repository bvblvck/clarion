# Generated by Django 3.2.6 on 2022-12-06 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_deposit_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance',
            name='user',
        ),
        migrations.RemoveField(
            model_name='deposit',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='deposit',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='deposit',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='deposit',
            name='token',
        ),
    ]