# from django.shortcuts import render,redirect
# from .models import Product, Order
# from seller.models import Category
# from buyer.models import Buyer
from django.shortcuts import render, redirect
from .models import Product, Order, Buyer
from seller.models import Category

def browse_products(request):
    categories = Category.objects.all()
    products = Product.objects.exclude(stock=0)
    return render(request, 'browse_products.html', {'categories': categories, 'products': products})

def view_category_products(request, category_id):
    categories = Category.objects.all()
    products = Product.objects.filter(category_id=category_id, stock__gt=0)
    return render(request, 'browse_products.html', {'categories': categories, 'products': products})

def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        buyer = Buyer.objects.get(user=request.user)
        product = Product.objects.get(pk=product_id)
        order, created = Order.objects.get_or_create(buyer=buyer)
        order.products.add(product)
        # Handle any additional logic or redirects
    return redirect('browse_products')

# def viewSure! Here's the remaining code for views and templates:

# **Views (continued):**

# ```python
# # buyer/views.py
def view_cart(request):
    if request.user.is_authenticated:
        buyer = Buyer.objects.get(user=request.user)
        order = Order.objects.filter(buyer=buyer).last()
        return render(request, 'view_cart.html', {'order': order})
    else:
        return redirect('login')
