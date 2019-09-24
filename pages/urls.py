from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('travel_deals', views.travel_deals, name='travel_deals'),
]