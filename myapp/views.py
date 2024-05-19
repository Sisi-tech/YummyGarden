from django.shortcuts import render, get_object_or_404
from .models import Menu 
from .models import Drinks 
from .forms import BookingForm
from django.contrib import messages 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import DrinksSerializer
from django.core.paginator import Paginator, EmptyPage
from .models import Dessert 

# Create your views here.
def home(request):
    home_content = {"home": "Welcome to SCoffee!! Enjoy your time 😉"}
    return render(request, "home.html", home_content)

def about(request):
    return render(request, "about.html")

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


def menu(request):
    menu_data = Menu.objects.all()
    drinks_data = Drinks.objects.all()
    dessert_data = Dessert.objects.all()
    context = {"menu": menu_data, "drinks": drinks_data, "desserts": dessert_data}
    return render(request, "menu.html", context)

def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {"menu_item": menu_item})


def display_drink_item(request, pk=None):
    drink_item = get_object_or_404(Drinks, pk=pk)
    return render(request, 'drink_item.html', {"drink_item": drink_item})

def dessert(request, pk=None):
    dessert_item = get_object_or_404(Dessert, pk=pk)
    return render(request, 'dessert_item.html', {'dessert': dessert_item})


class DrinksList(APIView):
    def get(self, request):
        drinks = Drinks.objects.select_related('category').all()
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', default=1)
        if category_name:
            drinks = drinks.filter(category__title=category_name)
        if to_price:
            drinks = drinks.filter(price_lte=to_price)
        if search:
            drinks = drinks.filter(title__icontains=search)
        if ordering:
            ordering_fields = ordering.split(",")
            drinks = drinks.order_by(*ordering_fields)

        paginator = Paginator(drinks, per_page=perpage)
        try:
            drinks = paginator.page(number=page)
        except EmptyPage:
            drinks = []
            
        serializer = DrinksSerializer(drinks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = DrinksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class Drink(APIView):
    def get(self, request, pk):
        drink = Drinks.objects.get(pk=pk)
        serializer = DrinksSerializer(drink)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        drink = Drinks.objects.get(pk=pk)
        serializer = DrinksSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        drink = Drinks.objects.get(pk=pk)
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    