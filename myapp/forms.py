from django import forms
from django.forms import modelformset_factory
from .models import Booking, Review, ReviewImage
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

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review 
        fields = ["first_name", "last_name", "review"]

class ReviewImageForm(forms.ModelForm):
    class Meta:
        model = ReviewImage
        fields = ["image"]

ReviewImageFormSet = modelformset_factory(ReviewImage, form=ReviewImageForm, extra=4)
