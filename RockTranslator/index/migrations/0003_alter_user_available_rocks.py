# Generated by Django 4.1 on 2022-09-02 15:29

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_user_exp_alter_user_available_rocks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='available_rocks',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None),
        ),
    ]
