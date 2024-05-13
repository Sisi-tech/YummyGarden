from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .models import Menu 
from .forms import BookingForm
from django.contrib import messages 


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


