<p align="center">
      <img src="https://upload.wikimedia.org/wikipedia/commons/5/50/Silpo.png" width="300" height="100">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/Django%20-4.1.3-red">
   <img src="https://img.shields.io/badge/Django--allauth-0.52.0-blue">
   <img src="https://img.shields.io/badge/License-MIT-brightgreen">
</p>


## About the project

In this project, I tried to reproduce Silpo's site. Implemented various transitions, category selection and product selection from the category. Registration completed. As well as the withdrawal of goods to the basket and the purchase of the selected product. And also connected some JS code for a beautiful design.

## Documentation

Description of routes:

- "An empty path that displays the main page. View class: views.ProductsView.as_view() URL name: 'home'" <br>
- " 'search/': Path to search for products. View class: views.Search.as_view() URL name: 'search' " <br>
- " '<slug:slug>': Path for displaying detailed information about the product, where <slug:slug> is the product slug. View class: views.ProductDatailView.as_view() URL Name: 'data' " <br>
- " 'country/<str:slug>': Path to display information about the country, where <str:slug> is the slug of the country. View class: views.CountryDatailView.as_view() URL name: 'country' " <br>
- " 'category/<slug:cat_slug>/': The path to display products for the selected category, where <slug:cat_slug> is the category slug. View class: views.PostCategoryView.as_view() URL name: 'category' " <br>
- " 'add rating/': The way to add a rating to a product. View class: views.AddStarsRating.as_view() URL name: 'add_rating' " <br>
- " 'comments/<int:pk>/': Path for adding a comment to the product, where <int:pk> is the product ID. View class: views.AddComments.as_view() URL name: 'add_comments' " <br>

Description View:

- " mix: The base view class that adds categories to the data context. Methods: get_context_data(*args, **kwargs): Method for adding categories to the data context. Returns the updated data context. " <br>
- " Products View: View class for displaying a list of products. Inherits: Mix, ListView Model: Product Attributes: queryset: Query to get a list of products, excluding those with draft set to True. " <br>
- " Search: View class for searching products. Inherits: ListView Methods: get_queryset(): Method for getting a list of products filtered by the presence of a search query in the product title. " <br>
- " ProductDataView: View class for displaying complete product information. Inherits: Mix, DetailView Model: Product Attributes: slug_field: Product model field used to get the product slug. Methods: get_context_data(**kwargs): Method for adding the rating form to the data context. Returns the updated data context. " <br>
- " Country Data View: View class for displaying country information. Inherits: Mix, DetailView Model: Manufacturer Attributes: template_name: The name of the template used to display country data. slug_field: A field in the Manufacturer model used to get the country slug. " <br>
- " PostCategoryView: View class for displaying a list of products for the selected category. Inherits: Mix, ListView Model: Product Attributes: template_name: The name of the template used to display the list of products. Methods: get_queryset(): Method for getting a list of products filtered by the selected category and excluding those with draft equal to True. " <br>
- " AddStarsRating: View class for adding rating to products. Inherits: View Methods: get_client_ip(request): A method to get the client's IP address from a request. "


## Developers

- [Vitaliy Zhankov] (https://github.com/ZhankovVG)

## P.S. Thank you for reading and visiting my repository, have a nice day!
