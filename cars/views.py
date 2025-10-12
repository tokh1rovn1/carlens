from django.shortcuts import render
from .models import Car, Category
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView

# Create your views here.

class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars'

class CarCreateView(CreateView):
    model = Car
    template_name = 'car_form.html'
    fields = ['name', 'category', 'price', 'image', 'description']
    success_url = reverse_lazy('car_list')



