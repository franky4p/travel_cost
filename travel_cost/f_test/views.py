from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

import app.utils as ut 

def index(request):
    now = datetime.now()
    hotels = ut.get_hotel()

    var_dict = {"title": "Find",  
                "year": datetime.now().year,
                "hotels": hotels,}

    return render(request, "index.html", var_dict)