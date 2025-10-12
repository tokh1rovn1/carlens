from django.urls import path
from .views import CarListView, CarCreateView

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('cars/add/', CarCreateView.as_view(), name='car_create'),
]