# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0005_auto_20170828_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='checkin_time_time',
            field=models.TimeField(default=datetime.datetime(2017, 8, 28, 18, 29, 43, 710326, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
