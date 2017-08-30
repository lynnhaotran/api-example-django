# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0002_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='checkin_time',
            field=models.TimeField(default=datetime.time(5, 9, 5, 156479)),
        ),
    ]
