# Generated by Django 4.2 on 2023-05-25 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0008_bookinstance_borrower'),
    ]

    operations = [
        migrations.AddField(
            model_name='bag',
            name='Basket',
            field=models.ForeignKey(blank=True, help_text='Выберите заказчика сумки', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Заказчик'),
        ),
    ]
