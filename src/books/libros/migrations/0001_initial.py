# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0001_initial'),
        ('editoriales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoresHasLibros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Autores_id', models.ForeignKey(to='autores.Autores')),
            ],
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('isbn', models.CharField(max_length=13, serialize=False, primary_key=True, validators=[django.core.validators.RegexValidator(regex=b'^.{13}$', message='El largo debe ser de 13', code=b'nomatch'), django.core.validators.RegexValidator(regex=b'^[0-9]+$', message='Un ISBN solo debe contener numeros', code=b'nomatch')])),
                ('titulo', models.CharField(max_length=45)),
                ('sinopsis', models.TextField()),
                ('n_paginas', models.CharField(max_length=45, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]+$', message='Un ISBN solo debe contener numeros', code=b'nomatch')])),
                ('editorial', models.ForeignKey(to='editoriales.Editoriales')),
            ],
        ),
        migrations.AddField(
            model_name='autoreshaslibros',
            name='libros_isbn',
            field=models.ForeignKey(to='libros.Libros'),
        ),
    ]
