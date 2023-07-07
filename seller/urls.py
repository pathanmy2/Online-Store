from django.urls import path
from . import views

urlpatterns = [
    path('add_product/', views.add_product, name='seller_add_product'),
    path('view_products/', views.view_products, name='seller_view_products'),
]
