# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0009_auto_20170829_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='token_expiration',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
