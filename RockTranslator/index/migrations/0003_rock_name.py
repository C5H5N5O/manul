# Generated by Django 4.0.6 on 2022-08-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_rock_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='rock',
            name='name',
            field=models.CharField(default='Valentin', max_length=40),
        ),
    ]
