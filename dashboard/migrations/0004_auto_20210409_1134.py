# Generated by Django 3.1.7 on 2021-04-09 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20210409_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countrydata',
            old_name='Day',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='countrydata',
            old_name='Count',
            new_name='population',
        ),
    ]
