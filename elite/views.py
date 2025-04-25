from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


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

    return render(request, 'catalog.html', {'products': products})

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

def product(request):
    return render(request, 'product_page.html')
