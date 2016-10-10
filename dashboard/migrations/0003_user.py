# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_messages_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fb_id', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=50)),
                ('batch', models.URLField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
