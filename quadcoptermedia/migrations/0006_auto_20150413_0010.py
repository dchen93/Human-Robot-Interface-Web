# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quadcoptermedia', '0005_auto_20150413_0008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploaddate',
            old_name='upload_date',
            new_name='upload_batch',
        ),
    ]
