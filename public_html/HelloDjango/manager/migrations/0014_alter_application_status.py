# Generated by Django 4.1.5 on 2023-01-07 17:52

from django.db import migrations, models
import django.db.models.deletion
import manager.models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0013_alter_application_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.ForeignKey(default=manager.models.get_def_status_application, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.applicationstatus', verbose_name='Статус заявки'),
        ),
    ]
