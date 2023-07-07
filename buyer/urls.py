from django.urls import path
from . import views


urlpatterns = [
    path('browse_products/', views.browse_products, name='browse_products'),
    path('category/<int:category_id>/', views.view_category_products, name='view_category_products'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
]
