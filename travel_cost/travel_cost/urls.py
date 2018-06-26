"""
Definition of urls for travel_cost.
"""

from datetime import datetime
from django.urls import path
import django.contrib.auth.views

import app.forms
import app.views

#учусь
import f_test.views

# Uncomment the next lines to enable the admin:
 #from django.conf.urls import include
 #from django.contrib import admin
 #admin.autodiscover()

urlpatterns = [

    #учусь
    path('hiDjango', f_test.views.index, name='index'),
    #url(r'^home$', f_test.views.index, name='home'),

    # Examples:
     path('', app.views.home, name='home'),
     path('contact', app.views.contact, name='contact'),
     path('about', app.views.about, name='about'),
    path('login/', django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    path('logout', django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
]
