from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name

class Drinks(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=None)
    def __str__(self):
        return self.title 

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    reservation_time = models.DateTimeField(auto_now=True)
    comments = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
        
class Menu(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return self.name 
