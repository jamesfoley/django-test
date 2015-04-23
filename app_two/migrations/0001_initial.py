# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import file.fields


class Migration(migrations.Migration):

    dependencies = [
        ('file', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelTwo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', file.fields.FileRefField(related_name='+', on_delete=django.db.models.deletion.PROTECT, blank=True, to='file.File', null=True)),
            ],
        ),
    ]
