# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-10 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('underTheaterApp', '0003_ticket_ticketeable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datetimefunction',
            name='until',
            field=models.DateField(blank=True, null=True),
        ),
    ]
