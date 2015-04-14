# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_path', models.FileField(upload_to=b'%Y/%m')),
            ],
        ),
        migrations.CreateModel(
            name='UploadDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload_date', models.DateField(default=datetime.date(2015, 4, 12), verbose_name=b'Date Uploaded')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='date',
            field=models.ForeignKey(to='quadcoptermedia.UploadDate'),
        ),
    ]
