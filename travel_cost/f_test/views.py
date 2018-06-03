from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()
    var_dict = {"title": "Hello Django", "message": "again Hello", "content": " on " + now.strftime("%A, %d %B, %Y at %X")}
    
    return render(request, "index.html", var_dict)