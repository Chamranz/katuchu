from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class ImageBag (models.Model):
    image = models.ImageField (verbose_name="Картинка сумки", null=True,upload_to='images/')
    def __str__(self):
        return self.image

class colours(models.Model):
    name = models.CharField(max_length=200, help_text="Введите цвет сумки", verbose_name="Цвет сумки")

    def __str__(self):
        return self.name

class material(models.Model):
    name = models.CharField (max_length=20, help_text="Введите материалы сумки", verbose_name='Материалы сумки')

    def __str__(self):
        return self.name

class cost(models.Model):
    name = models.CharField (max_length=20, help_text="Введите стоимость сумки", verbose_name='Стоимость сумки')

    def __str__(self):
        return self.name
    
class Bag(models.Model):
    image = models.ImageField(help_text='Загрузите изображение', verbose_name='Картинка сумки', null=True,upload_to='media')
    title = models.CharField(max_length=200, help_text='Введите название сумки',verbose_name='Название сумки')
    colours = models.ForeignKey('Colours', on_delete=models.CASCADE, max_length=20, verbose_name='Цвет сумки')
    material = models.ForeignKey('Material', on_delete=models.CASCADE, max_length=200, verbose_name='Материалы сумки')
    summary = models.CharField(max_length=1000, help_text='',verbose_name='Введите описание сумки')
    cost = models.CharField(max_length=20, help_text='Стоимость сумки', null=True)
    status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True,
                               verbose_name='Статус экземпляра')
    Basket = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Заказчик',
                                 help_text='Выберите заказчика сумки')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('bag-detail', args=[str(self.id)])
    
class Status(models.Model):
    name = models.CharField(max_length=20, help_text="Введите статус экземпляра сумки", verbose_name='Статус экземпляра')

    def __str__(self):
        return self.name

class BookInstance (models.Model):


    bag = models.ForeignKey('Bag', on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(max_length=20, null=True, help_text="Введите номер экспемпляра", verbose_name='Номер экземпляра')
    status = models.ForeignKey ('Status', on_delete=models.CASCADE, null=True, help_text="Изменить состояние экземпляра", verbose_name='Статус экземпляра')
    due_back = models.DateField(null=True, blank=True, help_text="Введите конец срока статуса", verbose_name="Дата окончания статуса")
    borrower = models.ForeignKey (User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Заказчик',
                                  help_text='Выберите заказчика сумки')
    def __str__(self):
        return "%s %s %s" % (self.inv_nom, self.bag, self.status)

class Modification (models.Model):
    crest = models.ImageField(help_text='Загрузите изображение', verbose_name='Картинка крестика', null=True,upload_to='media')
    textfield = models.CharField(verbose_name='тестовый текст', max_length=20, null=True)



