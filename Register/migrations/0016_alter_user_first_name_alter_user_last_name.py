# Generated by Django 4.0.3 on 2022-07-07 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0015_user_check_transportation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='last name'),
        ),
    ]
