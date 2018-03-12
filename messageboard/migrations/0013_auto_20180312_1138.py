# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0012_auto_20180312_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mess',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 12, 11, 38, 2, 380370, tzinfo=utc)),
        ),
    ]
