# Generated by Django 4.2 on 2023-05-02 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_bag_image_alter_imagebag_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagebag',
            name='image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Картинка сумки'),
        ),
    ]
