# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0012_auto_20170830_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='start_time',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
