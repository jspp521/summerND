# Generated by Django 2.0.6 on 2018-07-04 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netdisk2', '0005_auto_20180628_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='owner_name',
            field=models.CharField(default='admin', max_length=200),
        ),
    ]