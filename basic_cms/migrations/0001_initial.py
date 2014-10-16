# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('stub', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('article', models.ForeignKey(to='basic_cms.Page')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pages', models.ManyToManyField(to='basic_cms.Page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
