from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.forms.formsets import formset_factory
from f_test.forms import NameForm, PersonalTable, InlineForm, FieldsetField

import app.utils as ut 

dict_plan = {}

# Стандартный formset
InlineFormSet = formset_factory(InlineForm, extra=2)

def index(request):

    form = NameForm()

    var_dict = {"title": "Find",  
                "year": datetime.now().year,
                "form": form,}
    
    if request.method == 'POST':
        formset = InlineFormSet(request.POST, prefix='formset')

        form = NameForm(request.POST)

        if form.is_valid():
            ch_field = form.cleaned_data["choice_field"]
            city = form.cleaned_data["city"]

            dict_plan[form.cleaned_data["my_date"]] = {"city": city}

            action = request.POST.get('action')
            if action == 'done':
                arr = [request.POST.get(key) for key in request.POST.keys() if 'check_column' in key]
               
        hotels = ut.get_info(ch_field, city)
       
        table = PersonalTable(hotels)

        dict_hotel = {hotels.index(a)+1:a for a in hotels}

        var_dict = {"title": "Find",  
                    "year": datetime.now().year,
                    "plan": dict_plan,
                    "hotels": dict_hotel,
                    "form": form,
                    "table": table}
        
    return render(request, "index.html", var_dict)