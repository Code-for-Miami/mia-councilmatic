# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('councilmatic_core', '0010_auto_20160120_1248'),
        ('miamidade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiamiDadeEvent',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('councilmatic_core.event',),
        ),
    ]
