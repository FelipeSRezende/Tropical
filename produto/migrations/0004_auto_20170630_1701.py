# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-30 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_auto_20170521_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estabelecimentoproduto',
            name='data_inicio_promocao',
            field=models.DateField(blank=True, null=True),
        ),
    ]
