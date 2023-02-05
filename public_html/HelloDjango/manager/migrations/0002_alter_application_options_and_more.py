# Generated by Django 4.1.3 on 2022-11-06 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterModelOptions(
            name='applicationmaterial',
            options={'verbose_name': 'Заявка на материал', 'verbose_name_plural': 'Заявки на материалы'},
        ),
        migrations.AlterModelOptions(
            name='applicationstatus',
            options={'verbose_name': 'Статус заявки', 'verbose_name_plural': 'Статусы заявок'},
        ),
        migrations.AlterModelOptions(
            name='applicationtechnic',
            options={'verbose_name': 'Заявка на технику', 'verbose_name_plural': 'Заявки на технику'},
        ),
        migrations.AlterModelOptions(
            name='constructionsite',
            options={'verbose_name': 'Строительный объект', 'verbose_name_plural': 'Строительные объекты'},
        ),
        migrations.AlterModelOptions(
            name='materialtarget',
            options={'verbose_name': 'Назначение материала', 'verbose_name_plural': 'Назначение материалов'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterModelOptions(
            name='technic',
            options={'verbose_name': 'Техника', 'verbose_name_plural': 'Техника'},
        ),
        migrations.AlterModelOptions(
            name='technicstamp',
            options={'verbose_name': 'Марка техники', 'verbose_name_plural': 'Марки техники'},
        ),
        migrations.AlterModelOptions(
            name='technicstatus',
            options={'verbose_name': 'Состояние техники', 'verbose_name_plural': 'Состояния техники'},
        ),
        migrations.AlterModelOptions(
            name='technictype',
            options={'verbose_name': 'Тип техники', 'verbose_name_plural': 'Типы техники'},
        ),
        migrations.RemoveField(
            model_name='applicationtechnic',
            name='load_capacity',
        ),
        migrations.RemoveField(
            model_name='applicationtechnic',
            name='stamp',
        ),
        migrations.RemoveField(
            model_name='applicationtechnic',
            name='type',
        ),
        migrations.AddField(
            model_name='applicationtechnic',
            name='vehicle',
            field=models.CharField(default=1, max_length=255, verbose_name='Название техники'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technic',
            name='load_capacity',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Грузоподъемность'),
        ),
        migrations.AddField(
            model_name='technic',
            name='stamp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.technicstamp', verbose_name='Марка'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.CharField(max_length=255, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.post', verbose_name='Категория'),
        ),
    ]
