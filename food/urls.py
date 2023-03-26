from django.urls import path
from .import views


urlpatterns = [
    path('', views.ProductsView.as_view(), name='home'),
    path('search/', views.Search.as_view(), name='search'),
    path('<slug:slug>', views.ProductDatailView.as_view(), name='datail'),
    path('country/<str:slug>', views.CountryDatailView.as_view(), name='country'),
    path('category/<slug:slug>/', views.PostCategoryView.as_view(), name='category'),
    path('add-rating/', views.AddStarsRating.as_view(), name='add_rating'),
]
