# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bloodbank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField(default=None)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('password', models.CharField(default=None, max_length=20)),
                ('user', models.OneToOneField(default=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
