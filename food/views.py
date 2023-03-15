from django.shortcuts import render
from django.views.generic import ListView
from .models import *



class ProductsView(ListView):
    model = Product
    queryset = Product.objects.filter(draft=False)
    template_name = 'food/product_list.html'