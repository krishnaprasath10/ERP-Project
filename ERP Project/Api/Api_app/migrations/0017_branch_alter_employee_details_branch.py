# Generated by Django 4.1.5 on 2023-06-26 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api_app', '0016_designation_alter_employee_details_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Branch', models.CharField(max_length=100)),
                ('Is_Head', models.BooleanField(default=False)),
                ('Location', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='employee_details',
            name='Branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Api_app.branch'),
        ),
    ]
