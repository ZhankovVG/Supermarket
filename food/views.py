from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *



class ProductsView(ListView):
    model = Product
    queryset = Product.objects.filter(draft=False)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context
        


class Search(ListView):
    # поиск продуктов
    def get_queryset(self):
        return Product.objects.filter(title__icontains =self.request.GET.get('search'))
    

class ProductDatailView(DetailView):
    # полное описание продукта
    model = Product
    slug_field = 'url'


class CountryDatailView(DetailView):
    model = Manufacturer
    template_name = 'food/country.html'
    slug_field = 'name'

 