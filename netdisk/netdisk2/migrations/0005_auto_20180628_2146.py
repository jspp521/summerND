# Generated by Django 2.0.6 on 2018-06-28 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netdisk2', '0004_filemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='myfile',
            field=models.FileField(upload_to='ert'),
        ),
    ]
