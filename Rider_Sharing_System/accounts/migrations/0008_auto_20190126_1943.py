# Generated by Django 2.1.5 on 2019-01-26 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_ride_driver_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='driver_id',
            field=models.IntegerField(default='0'),
        ),
    ]