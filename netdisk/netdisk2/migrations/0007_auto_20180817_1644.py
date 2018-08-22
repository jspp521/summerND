# Generated by Django 2.0.6 on 2018-08-17 08:44

from django.db import migrations, models
import netdisk2.models


class Migration(migrations.Migration):

    dependencies = [
        ('netdisk2', '0006_filemodel_owner_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='myfile',
            field=models.FileField(upload_to=netdisk2.models.fileModel.report_path),
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
