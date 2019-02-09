# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
                ('image', models.FileField(upload_to='sandeep/static/img/profile/')),
                ('about', models.TextField(null=True)),
                ('password', models.CharField(max_length=100)),
                ('address', models.TextField(null=True)),
                ('phone', models.CharField(max_length=30)),
                ('fb', models.CharField(default='https://www.facebook.com/sandeep.bangarh', max_length=100)),
                ('twitter', models.CharField(default='', max_length=100)),
                ('github', models.CharField(default='https://github.com/sanbangarh309', max_length=100)),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('client', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=50)),
                ('user_id', models.IntegerField()),
                ('image', models.FileField(upload_to='sandeep/static/img/projects/')),
                ('about', models.TextField(null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('about', models.TextField(null=True)),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
    ]