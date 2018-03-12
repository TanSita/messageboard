# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mess',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('content', models.TextField(default='')),
                ('date', models.DateTimeField(default=datetime.datetime(2018, 3, 12, 7, 18, 29, 519661, tzinfo=utc))),
            ],
        ),
    ]
