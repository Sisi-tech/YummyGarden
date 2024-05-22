from django.contrib import admin
from .models import Drinks, Category, Booking, Menu, Dessert, Cocktail, Review, ReviewImage 
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(Drinks)
admin.site.register(Category)
admin.site.register(Booking)
admin.site.register(Menu)
admin.site.register(Dessert)
admin.site.register(Cocktail)
admin.site.register(Review)
admin.site.register(ReviewImage)


class NewAdmin(UserAdmin):
    def get_form(self, request, obj=None, **Kwargs):
        form = super().get_form(request, obj, **Kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['username'].disabled = True

        return form
    

