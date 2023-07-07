
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category

@login_required
def add_product(request):
    if request.method == 'POST':
        seller = request.user
        category_id = request.POST['category']
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        stock = request.POST['stock']
        image = request.FILES['image']
        product = Product.objects.create(seller=seller, category_id=category_id, name=name,
                                         description=description, price=price, stock=stock, image=image)
        
        return redirect('seller_view_products')
    else:
        # Retrieve categories for dropdown
        categories = Category.objects.all()
        return render(request, 'add_product.html', {'categories': categories})

@login_required
def view_products(request):
    seller_products = Product.objects.filter(seller=request.user)
    return render(request, 'view_products.html', {'products': seller_products})
