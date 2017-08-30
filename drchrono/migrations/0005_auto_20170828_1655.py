# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0004_auto_20170828_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='checkin_time',
            field=models.DateTimeField(),
        ),
    ]
