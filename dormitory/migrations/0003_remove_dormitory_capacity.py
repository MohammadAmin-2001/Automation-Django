# Generated by Django 4.0.3 on 2022-07-04 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dormitory', '0002_rename_builing_name_dormitory_building_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dormitory',
            name='capacity',
        ),
    ]
