# Generated by Django 4.0.3 on 2022-03-18 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, default='', height_field=20, null=True, upload_to='Images/%Y/%m/%d/', verbose_name='image', width_field=20),
        ),
    ]