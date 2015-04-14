# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quadcoptermedia', '0006_auto_20150413_0010'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UploadDate',
            new_name='UploadBatch',
        ),
    ]
