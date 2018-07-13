import json
from django import forms
from django_select2.forms import HeavySelect2Widget
from django.contrib.auth import get_user_model

import django_tables2 as tables 

CHOICES = (('lodging', 'Отели',), ('museum', 'Музеи',), ('park', 'Парки',), ('shopping_mall', 'Магазины',))
COUNTRY_CHOICES = (("Россия", ("Россия")),("США", ("США")),("Канада", ("Канада")),("Япония", ("Япония")),("Сингапур", ("Сингапур")))

class NameForm(forms.Form):
    
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, required=False, label="Места")

    country = forms.ChoiceField(choices = COUNTRY_CHOICES, widget=HeavySelect2Widget(data_url='/url/to/json/response'), label="Страна", required=True)
    city = forms.CharField(required=False, max_length=100)
    my_date = forms.DateField(widget=forms.SelectDateWidget)
    
    
class PersonalTable(tables.Table):
    check_column = tables.CheckBoxColumn(empty_values=(), footer="", accessor='pk')
    name = tables.Column(verbose_name="Название", orderable=False)
    vicinity = tables.Column(verbose_name="Адрес", orderable=False) 

    class Meta:
        #template_name = "django_tables2/bootstrap4.html"
        attrs = {"class": "table table-hover"}