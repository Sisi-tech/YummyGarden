from rest_framework import serializers
from .models import Drinks 
from .models import Menu 
from .models import Booking
from .models import Dessert


class DrinksSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.category_name')
    
    class Meta:
        model = Drinks 
        fields = ['title', 'description', 'price', 'category']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu 
        fields = ['name', 'description', 'price']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking 
        fields = ['first_name', 'last_name', 'guest_count', 'reservation_time', 'comments']

class DessertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dessert
        fields = ['title', 'description', 'price']