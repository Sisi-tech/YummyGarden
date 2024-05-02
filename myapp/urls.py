from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="about"),
    path('menu/', views.menu, name="menu"),
    path('date/', views.display_date, name="date"),
]