from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>', views.display_menu_item, name="menu_item"),
    path('drink_item/<int:pk>', views.display_drink_item, name="drink_item"),
    path('api/drinks/', views.DrinksList.as_view()),
    path('api/drinks/<int:pk>', views.Drink.as_view()),
]