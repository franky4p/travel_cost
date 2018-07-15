import json
from django import forms
from django_select2.forms import HeavySelect2Widget
from django.contrib.auth import get_user_model

import django_tables2 as tables 

CHOICES = (('lodging', 'Отели',), ('museum', 'Музеи',), ('park', 'Парки',), ('shopping_mall', 'Магазины',))
COUNTRY_CHOICES = (("Россия", ("Россия")),("США", ("США")),("Канада", ("Канада")),("Япония", ("Япония")),("Сингапур", ("Сингапур")))
CITY_CHOICES = (("Москва", ("Москва")),("Вашингтон", ("Вашингтон")), ("Токио", ("Токио")))

class FieldsetField(forms.Field):
    # Поле формы, содержащее другую форму
    def __init__(self, fieldset, *args, **kwargs):
        # Html формы передается параметром этого виджета
        widget = FieldsetWidget(attrs={
            'form_html': '<table>%s</table>' % fieldset.as_table()
        })
        kwargs.update({
            'widget': widget,
            'required': False
        })
        super(FieldsetField, self).__init__(*args, **kwargs)


class InlineForm(forms.Form):
    # Вложенная форма
    name = forms.CharField(label='файл')
    vicinity = forms.CharField(label='название')


class NameForm(forms.Form):
    
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, required=False, label="Места")

    country = forms.ChoiceField(choices = COUNTRY_CHOICES, widget=HeavySelect2Widget(data_url='/url/to/json/response'), label="Страна", required=True)
    city = forms.ChoiceField(choices = CITY_CHOICES, widget=HeavySelect2Widget(data_url='/url/to/json/response'), label="Город", required=True)
    my_date = forms.DateField(widget=forms.SelectDateWidget)
    


class PersonalTable(tables.Table):
    check_column = tables.CheckBoxColumn(empty_values=(), footer="", accessor='pk')

    name = tables.Column(verbose_name="Название", orderable=False)
    vicinity = tables.Column(verbose_name="Адрес", orderable=False) 

    class Meta:
        #template_name = "django_tables2/bootstrap4.html"
        attrs = {"class": "table table-hover"}
        #row_attrs = {'data-id': lambda record: "1"}



