# Generated by Django 3.2.6 on 2022-12-30 20:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_remove_deposit_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=299.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='order_id',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4),
        ),
    ]
