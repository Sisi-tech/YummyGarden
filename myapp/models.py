from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name

class Drinks(models.Model):
    title = models.CharField(max_length=200, default="")
    description = models.TextField(max_length=1000, default="")
    price = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=None)
    url = models.ImageField(upload_to='drinks')
    def __str__(self):
        return self.title 

        
class Menu(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    url = models.ImageField(upload_to='menu')

    def __str__(self):
        return self.name 
    
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    reservation_time = models.DateTimeField(auto_now=True)
    comments = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Dessert(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, default="")
    price = models.DecimalField(max_digits=4, decimal_places=2, null=False)
    url = models.ImageField(upload_to='dessert')
    
    def __str__(self):
        return self.title
    
class Cocktail(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, default="")
    price = models.DecimalField(max_digits=4, decimal_places=2, null=False)
    url = models.ImageField(upload_to='cocktails')

    def __str__(self):
        return self.title 

class Review(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    review = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ReviewImage(models.Model):
    review = models.ForeignKey(Review, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='reviews')

    def __str__(self):
        return f"Image for review by {self.review.first_name} {self.review.last_name}"

