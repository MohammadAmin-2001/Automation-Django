# Generated by Django 4.0.3 on 2022-05-10 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0007_alter_user_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='check_transportation',
            field=models.BooleanField(default=False),
        ),
    ]
