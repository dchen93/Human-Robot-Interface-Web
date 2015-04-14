# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quadcoptermedia', '0002_auto_20150412_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaddate',
            name='upload_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Date Uploaded'),
        ),
    ]
