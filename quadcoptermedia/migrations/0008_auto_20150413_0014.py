# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quadcoptermedia', '0007_auto_20150413_0012'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UploadBatch',
            new_name='UploadGroup',
        ),
        migrations.RenameField(
            model_name='uploadgroup',
            old_name='upload_batch',
            new_name='upload_group',
        ),
    ]
