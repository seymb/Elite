from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator


# Пример представления для главной страницы
def index(request):
    products = Product.objects.all().order_by('-created_at')  # все товары, если категории нет
    return render(request, 'main.html', {'products':products[:6]})

def catalog_view(request, category=None):
    if category:
        category_obj = Category.objects.filter(name__iexact=category).first()
        if category_obj:
            products = Product.objects.filter(category=category_obj)
        else:
            products = Product.objects.none()  # если категория не найдена
    else:
        products = Product.objects.all()  # все товары, если категории нет

    paginator = Paginator(products, 9)  # 9 товаров на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'catalog.html', {'page_obj': page_obj})

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'auth.html', {'error': 'Username already exists'})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('home')
    return render(request, 'auth.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            return redirect('home')  # или на главную
        else:
            return render(request, 'auth.html', {'error': 'Invalid credentials'})

    return render(request, 'auth.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def is_integer(value):
    return value % 1 == 0

def product(request, id=None):
    new_prices = []
    if id:
        prod = get_object_or_404(Product, id=id)
        prices = prod.prices.all()
        for price in prices:
            original_price = price.price

            original_price = int(original_price) if is_integer(original_price) else original_price
            price.discount = int(price.discount) if is_integer(price.discount) else price.discount
            if price.discount:
                new_price = original_price - (original_price * price.discount / 100)
                new_price = int(new_price) if is_integer(new_price) else new_price
                new_prices.append({'original_price': original_price, 'discount_price': new_price, 'volume': price.volume, 'discount': price.discount})
            else:
                new_prices.append({'original_price': original_price, 'discount_price': original_price, 'volume': price.volume, 'discount': 0})

    else:
        prod = None
        price = None
        new_prices = []
    return render(request, 'product_page.html', {'product': prod, 'prices': new_prices, 'id':id})