# Generated by Django 4.1.5 on 2023-06-30 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api_app', '0023_alter_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='Date',
            field=models.DateField(),
        ),
    ]
