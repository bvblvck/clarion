# Generated by Django 3.2.6 on 2022-11-28 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20221127_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='amount',
            field=models.CharField(default=0, max_length=9999),
        ),
        migrations.AddField(
            model_name='deposit',
            name='plan',
            field=models.CharField(default='starter', max_length=9999),
        ),
        migrations.AddField(
            model_name='deposit',
            name='token',
            field=models.CharField(default='bitcoin', max_length=9999),
        ),
    ]
