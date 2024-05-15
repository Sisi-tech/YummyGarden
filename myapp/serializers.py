from rest_framework import serializers
from .models import Drinks 


class DrinksSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category_id.category_name')
    
    class Meta:
        model = Drinks 
        fields = ['title', 'price', 'category_name']
