# Generated by Django 4.1.5 on 2023-06-23 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api_app', '0012_alter_employee_details_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_details',
            name='EPF_Number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee_details',
            name='Pan_Number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee_details',
            name='Previous_Company_Name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee_details',
            name='Reference_Name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee_details',
            name='Reference_Through',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
