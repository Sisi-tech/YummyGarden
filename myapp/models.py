from django.db import models

# Create your models here.
class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)

class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey(DrinksCategory, on_delete=models.PROTECT, default=None)
    def __str__(self):
        return self.drink

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Person(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

class Product(models.Model):
    ProductID: models.IntegerField()
    name: models.TextField()
    category: models.TextField()
    class Meta:
        permissions = [('can_change_category', 'Can change category')]
        
class Menu(models.Model):
    menuItem = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, default="")
    price = models.IntegerField()

    def __str__(self):
        return f"{self.menuItem}, {self.price}"
