from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *



class Mix:
    # Вывод категорий
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductsView(Mix, ListView):
    # Вывод продуктов
    model = Product
    queryset = Product.objects.filter(draft=False)

    
class Search(Mix, ListView):
    # поиск продуктов
    def get_queryset(self):
        return Product.objects.filter(title__icontains =self.request.GET.get('search'))
    

class ProductDatailView(Mix, DetailView):
    # полное описание продукта
    model = Product
    slug_field = 'url'


class CountryDatailView(Mix, DetailView):
    # Вывод стран
    model = Manufacturer
    template_name = 'food/country.html'
    slug_field = 'name'

 
class CategoryDetailView(Mix, DetailView):
    # Вывод категорий
    model = Category
    slug_field = 'url'
    