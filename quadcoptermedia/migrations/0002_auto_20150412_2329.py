# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quadcoptermedia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaddate',
            name='upload_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 13, 6, 29, 48, 255000, tzinfo=utc), verbose_name=b'Date Uploaded'),
        ),
    ]
