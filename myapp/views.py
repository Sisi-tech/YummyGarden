from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required

# Create your views here.
def home(request):
    return HttpResponse("Welcome to SCoffee")

def about(request):
    return HttpResponse("About us")

def menu(request):
    return HttpResponse("Menu for SCoffee")

def book(request):
    return HttpResponse("Make a booking")

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
