# Generated by Django 4.1.5 on 2023-06-22 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api_app', '0007_alter_employee_details_date_of_joining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_details',
            name='Phone_Number',
            field=models.IntegerField(null=True),
        ),
    ]
