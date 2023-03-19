from django.urls import path
from .import views


urlpatterns = [
    path('', views.ProductsView.as_view(), name='home'),
    path('search/', views.Search.as_view(), name='search'),
]
