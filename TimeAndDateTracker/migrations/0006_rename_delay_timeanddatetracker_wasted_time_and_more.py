# Generated by Django 4.0.3 on 2022-04-13 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TimeAndDateTracker', '0005_alter_timeanddatetracker_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timeanddatetracker',
            old_name='delay',
            new_name='wasted_time',
        ),
        migrations.RemoveField(
            model_name='timeanddatetracker',
            name='duration',
        ),
    ]