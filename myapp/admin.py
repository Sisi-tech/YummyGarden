from django.contrib import admin
from .models import Drinks
from .models import Category
from .models import Booking 
from django.contrib.auth.admin import UserAdmin
from .models import Menu 

# Register your models here.
admin.site.register(Drinks)
admin.site.register(Category)
admin.site.register(Booking)
admin.site.register(Menu)


class NewAdmin(UserAdmin):
    def get_form(self, request, obj=None, **Kwargs):
        form = super().get_form(request, obj, **Kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['username'].disabled = True

        return form
    

