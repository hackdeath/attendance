# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-24 17:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_attendance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fingerprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moment', models.DateTimeField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_attendance.Person')),
            ],
        ),
        migrations.CreateModel(
            name='WorkedTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finish', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='workedtime_finish', to='app_attendance.Fingerprint')),
                ('start', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workedtime_start', to='app_attendance.Fingerprint')),
            ],
        ),
        migrations.RemoveField(
            model_name='dedada',
            name='person',
        ),
        migrations.DeleteModel(
            name='Dedada',
        ),
    ]
