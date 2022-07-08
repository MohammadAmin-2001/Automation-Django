# Generated by Django 4.0.3 on 2022-07-07 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceCounter', '0004_alter_requestform_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestform',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('declined', 'Declined'), ('accepted', 'Accepted')], default='P', max_length=8),
        ),
    ]
