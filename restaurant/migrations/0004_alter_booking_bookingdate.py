# Generated by Django 4.1 on 2023-12-09 13:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_booking_bookingdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='BookingDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 9, 8, 58, 55, 602339)),
        ),
    ]