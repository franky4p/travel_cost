from django import forms


class NameForm(forms.Form):
    CHOICES = (('lodging', 'Отели',), ('museum', 'Музеи',), ('park', 'Парки',), ('shopping_mall', 'Магазины',))
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, required=False, label="Места")

    country = forms.CharField(required=False, max_length=100)
    city = forms.CharField(required=False, max_length=100)
    my_date = forms.DateField(required=False, widget=forms.SelectDateWidget)
    
    