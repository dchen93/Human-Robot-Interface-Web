# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quadcoptermedia', '0004_auto_20150412_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='uploaded_file',
            field=models.FileField(upload_to=b'%Y/%m/%d'),
        ),
    ]
