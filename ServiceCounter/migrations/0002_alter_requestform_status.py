# Generated by Django 4.0.3 on 2022-07-08 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceCounter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestform',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('declined', 'Declined'), ('accepted', 'Accepted')], default='pending', max_length=8),
        ),
    ]
