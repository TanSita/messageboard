# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mess',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 12, 7, 21, 36, 61111, tzinfo=utc)),
        ),
    ]
