from django.shortcuts import render, get_object_or_404, redirect
from .models import Menu, Drinks, Dessert, Cocktail, Review, ReviewImage
from .forms import BookingForm, ReviewForm, ReviewImageFormSet 
from django.contrib import messages 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import DrinksSerializer
from django.core.paginator import Paginator, EmptyPage


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
    cocktail_data = Cocktail.objects.all()
    dessert_data = Dessert.objects.all()
    context = {"menu": menu_data, "drinks": drinks_data, "desserts": dessert_data, "cocktails": cocktail_data}
    return render(request, "menu.html", context)

def display_menu_item(request, pk=None):
    menu_item = get_object_or_404(Menu, pk=pk)
    return render(request, 'menu_item.html', {"menu_item": menu_item})

def display_drink_item(request, pk=None):
    drink_item = get_object_or_404(Drinks, pk=pk)
    return render(request, 'drink_item.html', {"drink_item": drink_item})

def display_dessert_item(request, pk=None):
    dessert_item = get_object_or_404(Dessert, pk=pk)
    return render(request, 'dessert_item.html', {'dessert': dessert_item})

def display_cocktail_item(request, pk=None):
    cocktail_item = get_object_or_404(Cocktail, pk=pk)
    return render(request, 'cocktail_item.html', {"cocktail": cocktail_item})

def review(request):
    review_data = Review.objects.all() 
    reviewImage_data = ReviewImage.objects.all()
    context = {"reviews": review_data, "reviewImages": reviewImage_data}
    return render(request, 'review.html', context)

def display_review_item(request, pk=None):
    review_item = get_object_or_404(Review, pk=pk)
    review_image = get_object_or_404(ReviewImage, pk=pk)
    return render(request, 'review_item.html', {'review': review_item, 'review_image': review_image})

def review_success(request):
    return render(request, 'review_success.html')

def submit_review(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        formset = ReviewImageFormSet(request.POST, request.FILES, queryset=ReviewImage.objects.none())
        if review_form.is_valid() and formset.is_valid():
            review = review_form.save()
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = ReviewImage(review=review, image=image)
                    photo.save()
            return redirect('review_success')
    else:
        review_form = ReviewForm()
        formset = ReviewImageFormSet(queryset=ReviewImage.objects.none())
    return render(request, 'submit_review.html', {'review_form': review_form, 'formset': formset})


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
    
    
    
    