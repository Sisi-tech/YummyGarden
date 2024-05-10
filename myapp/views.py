from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .models import Menu 

# Create your views here.
def home(request):
    home_content = {"home": "Welcome to SCoffee!! Enjoy your time 😉"}
    return render(request, "home.html", home_content)

def about(request):
    about_content = {"about": "Welcome to SCoffee, your go-to destination for delightful coffee and indulgent desserts! Step into our cozy café and treat yourself to a world of flavor with our expertly crafted coffee creations and mouthwatering sweets. From rich espresso drinks to decadent cakes and pastries, every visit to SCoffee promises a moment of pure indulgence. Join us for a cozy atmosphere, friendly service, and a truly satisfying experience. Discover the perfect blend of coffee and sweetness at SCoffee today!"}
    return render(request, "about.html", about_content)

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, "menu.html", {"menu": main_data})

def book(request):
    return render(request, "book.html")

def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {"menu_item": menu_item})


