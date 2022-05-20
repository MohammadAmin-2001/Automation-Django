# Generated by Django 4.0.3 on 2022-05-18 17:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Register', '0008_user_check_transportation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('company', models.ManyToManyField(blank=True, to='Register.company')),
                ('user', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
