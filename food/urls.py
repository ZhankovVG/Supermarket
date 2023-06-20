from django.urls import path
from .import views


urlpatterns = [
    path('', views.ProductsView.as_view(), name='home'),
    path('search/', views.Search.as_view(), name='search'),
    path('<slug:slug>', views.ProductDatailView.as_view(), name='datail'),
    path('country/<str:slug>', views.CountryDatailView.as_view(), name='country'),
    path('category/<slug:cat_slug>/', views.PostCategoryView.as_view(), name='category'),
    path('add-rating/', views.AddStarsRating.as_view(), name='add_rating'),
    path('comments/<int:pk>/', views.AddComments.as_view(), name='add_comments'),
    path('signup/', views.CustomSignupView.as_view(), name='signup'),
]
