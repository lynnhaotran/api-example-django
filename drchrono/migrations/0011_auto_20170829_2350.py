# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0010_doctor_token_expiration'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='avg_wait_time',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='doctor',
            name='patients_seen',
            field=models.IntegerField(default=0),
        ),
    ]
