from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from f_test.forms import NameForm

import app.utils as ut 

def index(request):

    var_dict = {"title": "Find",  
                "year": datetime.now().year,}
    
    if request.method == 'POST':

        form = NameForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data["city"])
         
        #now = datetime.now()
        hotels = ut.get_hotel()
        dict_hotel = {hotels.index(a)+1:a for a in hotels}

        var_dict = {"title": "Find",  
                    "year": datetime.now().year,
                    "hotels": dict_hotel,
                    "form": form,}
        
    return render(request, "index.html", var_dict)