# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0013_auto_20180312_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='mess',
            name='username',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='mess',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 12, 11, 45, 17, 480983, tzinfo=utc)),
        ),
    ]
