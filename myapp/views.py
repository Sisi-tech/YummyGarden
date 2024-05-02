from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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


