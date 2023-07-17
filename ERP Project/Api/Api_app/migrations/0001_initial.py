# Generated by Django 4.1.5 on 2023-06-21 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_Name', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
                ('Date_Of_Birth', models.CharField(max_length=100)),
                ('Blood_Group', models.CharField(max_length=100)),
                ('Date_Of_Joining', models.CharField(max_length=100)),
                ('Phone_Number', models.CharField(max_length=100)),
                ('Email_Id', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=100)),
                ('Designation', models.CharField(max_length=100)),
                ('Qualification', models.CharField(max_length=100)),
                ('Current_Address', models.CharField(max_length=100)),
                ('Permanent_Address', models.CharField(max_length=100)),
                ('Aadhar_Number', models.CharField(max_length=100)),
                ('Pan_Number', models.CharField(max_length=100)),
                ('EPF_Number', models.CharField(max_length=100)),
            ],
        ),
    ]