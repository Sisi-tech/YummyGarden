from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required

# Create your views here.
def home(request):
    home_content = {"home": "Welcome to SCoffee!! Enjoy your time 😉"}
    return render(request, "home.html", home_content)

def about(request):
    about_content = {"about": "Welcome to SCoffee, your go-to destination for delightful coffee and indulgent desserts! Step into our cozy café and treat yourself to a world of flavor with our expertly crafted coffee creations and mouthwatering sweets. From rich espresso drinks to decadent cakes and pastries, every visit to SCoffee promises a moment of pure indulgence. Join us for a cozy atmosphere, friendly service, and a truly satisfying experience. Discover the perfect blend of coffee and sweetness at SCoffee today!"}
    return render(request, "about.html", about_content)

def menu(request):
    return render(request, "menu.html")

def book(request):
    return render(request, "book.html")

def display_date(request):
    date = datetime.today().year 
    return HttpResponse(date)

def myview(request):
    if request.user.is_anonymous():
        raise PermissionDenied()
    
@login_required
def login_required(request):
    return HttpResponse("Hello World")

def test_permission(user):
    if user.is_authenticated() and user.has_perm("myapp.change_category"):
        return True
    else:
        return False 
    
@user_passes_test(test_permission)
def change_ctg(request):
    pass 

@permission_required("myapp.change_category")
def store_creator(request):
    pass 
