# Generated by Django 4.0.3 on 2022-05-16 14:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ServiceCounter', '0002_requestuser_responseapi_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responseapi',
            name='admin',
        ),
        migrations.AddField(
            model_name='admintransportation',
            name='user',
            field=models.ManyToManyField(related_name='admintranslate_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='RequestUser',
        ),
        migrations.DeleteModel(
            name='ResponseApi',
        ),
    ]