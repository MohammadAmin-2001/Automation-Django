# Generated by Django 4.0.3 on 2022-03-15 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Register.company'),
        ),
    ]
