# Generated by Django 2.1.5 on 2019-01-26 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190126_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='isFinished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ride',
            name='isPicked',
            field=models.BooleanField(default=False),
        ),
    ]
