# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quadcoptermedia', '0003_auto_20150412_2332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='file_path',
            new_name='uploaded_file',
        ),
    ]
