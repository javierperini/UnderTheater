# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('underTheaterApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datetimeshow',
            name='datetime_show',
            field=models.DateTimeField(verbose_name='dia y horario del show'),
        ),
    ]