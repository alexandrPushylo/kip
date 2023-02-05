# Generated by Django 4.1.5 on 2023-01-04 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_alter_applicationtechnic_vehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationtechnic',
            name='driver',
            field=models.CharField(default='---', max_length=256, verbose_name='Вадитель'),
        ),
        migrations.AlterField(
            model_name='applicationtechnic',
            name='vehicle',
            field=models.CharField(max_length=256, verbose_name='Техника'),
        ),
    ]
