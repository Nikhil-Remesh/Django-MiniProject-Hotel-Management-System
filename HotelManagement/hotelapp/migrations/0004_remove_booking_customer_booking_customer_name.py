# Generated by Django 5.0.1 on 2024-02-07 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0003_alter_room_room_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='customer',
        ),
        migrations.AddField(
            model_name='booking',
            name='customer_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cust', to='hotelapp.customer'),
        ),
    ]
