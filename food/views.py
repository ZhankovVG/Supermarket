from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.views.generic import ListView, DetailView, View
from .models import *
from .forms import *
from cart.forms import CartAddProductForm
from .tasks import send_registration_email
from allauth.account.views import SignupView


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


class Search(ListView):
    # поиск продуктов
    def get_queryset(self):
        return Product.objects.filter(title__icontains=self.request.GET.get('search'))


class ProductDatailView(Mix, DetailView):
    # полное описание продукта
    model = Product
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['star_form'] = RatingForm()
        context['cart_product_form'] = CartAddProductForm
        return context


class CountryDatailView(Mix, DetailView):
    # Вывод стран
    model = Manufacturer
    template_name = 'food/country.html'
    slug_field = 'name'


class PostCategoryView(Mix, ListView):
    # вывод продуктов по гатегории
    model = Product
    template_name = 'food/product_list.html'

    def get_queryset(self):
        category = get_object_or_404(Category, url=self.kwargs['cat_slug'])
        return Product.objects.filter(category=category, draft=False)


class AddStarsRating(View):
    # Добавление рейтинга продуктам
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                product_id=int(request.POST.get("product")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)
        

class AddComments(View):
    # Отзывы
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        product = Product.objects.get(id = pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.product = product
            form.save()
        return redirect(product.get_absolute_url())
    
    
class CustomSignupView(SignupView):
    # Storing user registration information in Redis
    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get('email')
        send_registration_email.delay(email)
        return response