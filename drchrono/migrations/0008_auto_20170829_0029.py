# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0007_remove_patient_checkin_time_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='checkin_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
