# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0003_auto_20180312_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mess',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 12, 7, 54, 48, 696797, tzinfo=utc)),
        ),
    ]
