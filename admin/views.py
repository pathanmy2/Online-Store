
# from django.shortcuts import render
# from seller.models import Seller, Product
# from buyer.models import Buyer, Order
from seller.models import Seller, Product
from buyer.models import Buyer, Order

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
# from buyer.urls import buyer_browse_products

def view_sellers(request):
    sellers = Seller.objects.all()
    return render(request, 'view_sellers.html', {'sellers': sellers})

def view_products(request):
    products = Product.objects.all()
    return render(request, 'view_products.html', {'products': products})

def view_buyers(request):
    buyers = Buyer.objects.all()
    return render(request, 'view_buyers.html', {'buyers': buyers})

def view_orders(request):
    orders = Order.objects.all()
    return render(request, 'view_orders.html', {'orders': orders})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('buyer_browse_products')  
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

