# Generated by Django 4.1.5 on 2023-06-29 05:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api_app', '0017_branch_alter_employee_details_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(default=datetime.date.today)),
                ('Working_Hours', models.IntegerField(null=True)),
                ('Worked_Hours', models.IntegerField(null=True)),
                ('Over_Time', models.IntegerField(null=True)),
                ('Permission', models.IntegerField(null=True)),
                ('Casual_Leave', models.IntegerField(null=True)),
                ('Sick_Leave', models.IntegerField(null=True)),
                ('Status', models.CharField(max_length=100, null=True)),
                ('Employee_Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Api_app.employee_details')),
            ],
        ),
    ]
