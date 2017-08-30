# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0011_auto_20170829_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='avg_wait_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='wait_time',
            field=models.IntegerField(default=0),
        ),
    ]
