# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_auto_20161016_0101'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='videos/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='videoimage',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.Video'),
        ),
    ]
