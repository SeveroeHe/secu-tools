# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-13 03:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompilationPid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('taskid', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Compiler_conf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_os', models.CharField(max_length=60)),
                ('compiler', models.CharField(max_length=60)),
                ('version', models.CharField(max_length=60)),
                ('ip', models.CharField(max_length=60)),
                ('port', models.CharField(max_length=20)),
                ('http_path', models.CharField(max_length=60)),
                ('invoke_format', models.TextField()),
                ('flag', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile_conf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploader', models.CharField(max_length=200)),
                ('upload_time', models.DateTimeField()),
                ('name', models.CharField(max_length=200)),
                ('target_os', models.CharField(max_length=60)),
                ('compiler', models.CharField(max_length=60)),
                ('version', models.CharField(max_length=60)),
                ('flag', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProfileUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('srcCodes', models.FileField(blank=True, upload_to='hellomake')),
                ('content_type', models.CharField(max_length=50)),
                ('task_file', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('tag', models.TextField(blank=True, null=True)),
                ('src_file', models.CharField(max_length=200)),
                ('target_os', models.CharField(max_length=60)),
                ('compiler', models.CharField(max_length=60)),
                ('version', models.CharField(max_length=60)),
                ('flag', models.TextField()),
                ('exename', models.TextField(blank=True, null=True)),
                ('out', models.TextField(blank=True, null=True)),
                ('err', models.TextField(blank=True, null=True)),
                ('init_tmstmp', models.TextField()),
                ('finish_tmstmp', models.TextField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('tag', models.TextField(blank=True, null=True)),
                ('src_filename', models.CharField(max_length=200)),
                ('profiles', models.TextField()),
                ('target_os', models.TextField()),
                ('compiler_full', models.TextField()),
                ('compilation_num', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskFolder', models.CharField(max_length=200)),
                ('totalCompilation', models.IntegerField()),
                ('finishedCompilation', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
    ]
