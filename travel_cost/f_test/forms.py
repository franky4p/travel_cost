from django import forms
from django_select2.forms import HeavySelect2Widget

CHOICES = (('lodging', 'Отели',), ('museum', 'Музеи',), ('park', 'Парки',), ('shopping_mall', 'Магазины',))
COUNTRY_CHOICES = (("Россия", ("Россия")),("США", ("США")),("Канада", ("Канада")),("Япония", ("Япония")),("Сингапур", ("Сингапур")))
CITY_CHOICES = (("Москва", ("Москва")),("Вашингтон", ("Вашингтон")), ("Токио", ("Токио")))

class NameForm(forms.Form):
    
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, required=False, label="Места")

    country = forms.ChoiceField(choices = COUNTRY_CHOICES, widget=HeavySelect2Widget(data_url='/url/to/json/response'), label="Страна", required=True)
    city = forms.ChoiceField(choices = CITY_CHOICES, widget=HeavySelect2Widget(data_url='/url/to/json/response'), label="Город", required=True)
    my_date = forms.DateField(widget=forms.SelectDateWidget)
    


