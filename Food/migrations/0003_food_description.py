# Generated by Django 4.0.3 on 2022-07-05 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0002_food_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
