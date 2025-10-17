from django.urls import path
from .views import CarListView, CarCreateView, CarDetailView

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('cars/add/', CarCreateView.as_view(), name='car_create'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
]