# Generated by Django 4.1.5 on 2023-07-13 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api_app', '0028_alter_employee_details_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_details',
            name='Phone_Number',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
