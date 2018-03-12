# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0023_auto_20180312_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mess',
            name='content',
            field=models.TextField(default="I'm contents..."),
        ),
        migrations.AlterField(
            model_name='mess',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 12, 12, 30, 40, 383280, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mess',
            name='username',
            field=models.TextField(default='human :D'),
        ),
    ]
