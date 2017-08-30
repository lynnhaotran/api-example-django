# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0003_patient_checkin_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='wait_time',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='checkin_time',
            field=models.TimeField(default=datetime.time(16, 31, 49, 294236)),
        ),
    ]
