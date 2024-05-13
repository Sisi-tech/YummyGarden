from django import forms
from .models import Booking
from .models import Menu 
from django.core.validators import MinValueValidator, MaxValueValidator

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking 
        fields = '__all__'
        widgets = {
            'guest_count': forms.NumberInput(attrs={'min': 1, 'max': 12}),
        }
        validators = {
            'guest_count': [MinValueValidator(1), MaxValueValidator(12)],
        }

class MenuItems(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'