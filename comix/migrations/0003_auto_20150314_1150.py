# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comix', '0002_auto_20150314_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comicpost',
            name='image',
            field=models.ImageField(upload_to=b'static/img/comix'),
            preserve_default=True,
        ),
    ]
