from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()
    var_dict = {"title": "Find",  
                'year': datetime.now().year,}
    
    return render(request, "index.html", var_dict)