# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0004_remove_customer_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='age',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
    ]
