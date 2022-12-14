# Generated by Django 4.1 on 2022-09-02 13:31

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Massage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=40)),
                ('context', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Rock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Valentin', max_length=40)),
                ('hunger_index', models.IntegerField()),
                ('health_index', models.IntegerField()),
                ('happiness_index', models.IntegerField()),
                ('image', models.ImageField(default='https://cdn.discordapp.com/attachments/432562983776944150/1009574236261720074/3.png', upload_to='rocks/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('curent_rock', models.IntegerField()),
                ('available_rocks', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=8)),
            ],
        ),
    ]
