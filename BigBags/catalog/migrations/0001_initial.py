# Generated by Django 4.2 on 2023-04-17 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название сумки', max_length=200, verbose_name='Название сумки')),
                ('colours', models.CharField(help_text='Введите цвет сумки', max_length=20, verbose_name='Цвет сумки')),
                ('material', models.CharField(help_text='Введите материалы сумки', max_length=200, verbose_name='Материалы сумки')),
                ('summary', models.CharField(max_length=200, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='colours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите цвет сумки', max_length=200, verbose_name='Цвет сумки')),
            ],
        ),
        migrations.CreateModel(
            name='material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите материалы сумки', max_length=20, verbose_name='Материалы сумки')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите статус экземпляра сумки', max_length=20, verbose_name='Статус экземпляра')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_nom', models.CharField(help_text='Введите номер экспемпляра', max_length=20, null=True, verbose_name='Номер экземпляра')),
                ('due_back', models.DateField(blank=True, help_text='Введите конец срока статуса', null=True, verbose_name='Дата окончания статуса')),
                ('bag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.bag')),
                ('status', models.ForeignKey(help_text='Изменить состояние экземпляра', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.status', verbose_name='Статус экземпляра')),
            ],
        ),
    ]
