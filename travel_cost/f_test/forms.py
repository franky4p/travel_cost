from django import forms

class NameForm(forms.Form):
    country = forms.CharField(required=False, max_length=100)
    city = forms.CharField(required=False, max_length=100)
    my_date = forms.DateField(required=False)
    
    