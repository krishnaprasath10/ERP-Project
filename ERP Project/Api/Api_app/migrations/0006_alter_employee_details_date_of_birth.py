# Generated by Django 4.1.5 on 2023-06-22 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api_app', '0005_alter_employee_details_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_details',
            name='Date_Of_Birth',
            field=models.CharField(max_length=100),
        ),
    ]
