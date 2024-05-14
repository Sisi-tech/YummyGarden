from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu 
from .forms import BookingForm
from django.contrib import messages 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView


# Create your views here.
def home(request):
    home_content = {"home": "Welcome to SCoffee!! Enjoy your time 😉"}
    return render(request, "home.html", home_content)

def about(request):
    return render(request, "about.html")

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, "menu.html", {"menu": main_data})

def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # get form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            # capitalize first letter of first and last name
            form.instance.first_name = first_name.capitalize()
            form.instance.last_name = last_name.capitalize()
            form.save()
            messages.success(request, "Booking submitted successfully.")
    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form})


def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {"menu_item": menu_item})


@api_view(['GET', 'POST'])
def drinks(request):
    return Response('list of the drinks', status=status.HTTP_200_OK)

class DrinksList(APIView):
    def get(self, request):
        return Response({"message":"list of the drinks"}, status.HTTP_200_OK)
    def post(self, request):
        return Response({"message":"new drink created"}, status.HTTP_201_CREATED)
    
    
class Drink(APIView):
    def get(self, request, pk):
        return Response({"message":"single drink with id " + str(pk)}, status.HTTP_200_OK)
    def post(self, request, pk):
        return Response({"message":"single drink created with id " + str(pk)}, status.HTTP_201_CREATED)
    def delete(self, request, pk):
        return Response({"message":"single drink deleted with id " + str(pk)}, status.HTTP_301_MOVED_PERMANENTLY)
    def put(self, request, pk):
        return Response({"message":"single drink updated with id " + str(pk)}, status.HTTP_202_ACCEPTED)
    
    