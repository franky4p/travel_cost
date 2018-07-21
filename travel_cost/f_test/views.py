from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.forms.formsets import formset_factory
from f_test.forms import NameForm

import app.utils as ut 

dict_plan = {}

def index(request):
   
    if request.method == 'POST':

        form = NameForm(request.POST)

        if form.is_valid():
            ch_field = form.cleaned_data["choice_field"]
            city = form.cleaned_data["city"]
            my_date = form.cleaned_data["my_date"]

            hotels = ut.get_info(ch_field, city)
       
            dict_hotel = {hotels.index(a) + 1 : a for a in hotels}

            action = request.POST.get('action')
            if action == 'done':
                list_place = get_place(request.POST, my_date, dict_hotel)           
            
                dict_plan[my_date] = {"city": city, "list_place": list_place}
            
            var_dict = {
                        "title": "Find",  
                        "year": datetime.now().year,
                        "plan": dict_plan,
                        "hotels": dict_hotel,
                        "form": form,
                        }
    else:
        form = NameForm()

        var_dict = {
                    "title": "Find",  
                    "year": datetime.now().year,
                    "form": form,
                    }   
        
    return render(request, "index.html", var_dict)


def get_place(post, my_date, dict_hotel):
    selected_rows = [int(key[3:]) for key in post.keys() if 'ch_' in key]

    if dict_plan.get(my_date):
        list_place = dict_plan[my_date].get("list_place")
    else:
        list_place = []

    for row in selected_rows:     
        list_place.append(dict_hotel[row]) 

    return list_place
    