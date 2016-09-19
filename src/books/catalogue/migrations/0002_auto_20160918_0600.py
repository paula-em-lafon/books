# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='n_paginas',
            field=models.CharField(max_length=45, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]+$', message='Un ISBN solo debe contener numeros', code=b'nomatch')]),
        ),
    ]
