# Generated by Django 4.0.3 on 2022-05-20 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Notepad', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='file',
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notepad.note')),
            ],
        ),
    ]
