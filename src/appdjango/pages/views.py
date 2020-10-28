from django.shortcuts import render
from django.http import HttpResponse #PASO 1

# Create your views here.
def home_view(request, *args, **kwargs):#PASO 1 request paso2
    # return HttpResponse("<h1>Hello World</h1>") #string of html code #PASO 1
    return render(request, "home.html", {})#PASO2 {} context

def contact_view(request, *args, **kwargs):#PASO 2
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):#PASO 2
    return render(request, "about.html", {})

def social_view(request, *args, **kwargs):#PASO 2
    return HttpResponse("<h1>Social Page</h1>")