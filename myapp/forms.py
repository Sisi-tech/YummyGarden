from django import forms
from .models import Booking
from .models import Menu 

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking 
        fields = '__all__'

class MenuItems(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'