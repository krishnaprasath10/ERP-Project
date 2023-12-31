# Generated by Django 4.1.5 on 2023-06-30 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api_app', '0024_alter_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='Date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='Status',
            field=models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Casual', 'Casual'), ('Sick', 'Sick')], max_length=100, null=True),
        ),
    ]
