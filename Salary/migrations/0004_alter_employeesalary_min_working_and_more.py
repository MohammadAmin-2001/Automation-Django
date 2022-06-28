# Generated by Django 4.0.3 on 2022-06-19 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Salary', '0003_remove_employeesalary_price_dormitory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeesalary',
            name='min_working',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='employeesalary',
            name='monthly_salary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='employeesalary',
            name='reward_benefit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]