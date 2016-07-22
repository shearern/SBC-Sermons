# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 01:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoverImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cover_images')),
            ],
        ),
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recorded_at', models.DateField()),
                ('title', models.CharField(max_length=120)),
                ('hidden', models.BooleanField(default=False)),
                ('cover_image', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='sbc_sermons.CoverImage')),
            ],
        ),
        migrations.CreateModel(
            name='SbcClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='recording',
            name='sbc_class',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='sbc_sermons.SbcClass'),
        ),
        migrations.AddField(
            model_name='recording',
            name='series',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='sbc_sermons.Series'),
        ),
        migrations.AddField(
            model_name='recording',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sbc_sermons.Session'),
        ),
        migrations.AddField(
            model_name='recording',
            name='speakers',
            field=models.ManyToManyField(blank=True, to='sbc_sermons.Speaker'),
        ),
    ]