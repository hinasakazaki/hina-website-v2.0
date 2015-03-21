# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comix', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comicpost',
            name='image',
            field=models.ImageField(upload_to=b'comix/img'),
            preserve_default=True,
        ),
    ]
