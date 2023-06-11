from django import forms
from .models import Bag

class BagForm (forms.ModelForm):
    class Meta:
        model = Bag
        fields = ('colours', 'material','status')

class ChooseColor(forms.Form):
    colour_brown = forms.BooleanField (label="Коричневый")
    colour_black = forms.BooleanField (label='Черный')
    colour_white = forms.BooleanField (label='Белый')
    colour_whity = forms.BooleanField (label='Бежевый')

class ChooseMaterial(forms.Form):
    cloth = forms.BooleanField(label='Ткань')
    wood = forms.BooleanField(label='Дерево')

class ChooseStatus(forms.Form):
    Yet=forms.BooleanField(label="На складе")
    Reservation= forms.BooleanField(label='Зарезервирован')
    NotYet=forms.BooleanField(label="Нет в наличии")

class UserForm(forms.Form):
    email=forms.EmailField(label='Укажите ваш email адрес')
    reklama = forms.BooleanField(label='Согласны получать рекламу', required=False)

