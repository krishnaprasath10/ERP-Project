# Generated by Django 4.1.5 on 2023-07-13 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api_app', '0027_alter_employee_details_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_details',
            name='Phone_Number',
            field=models.IntegerField(null=True),
        ),
    ]
