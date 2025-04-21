from django.shortcuts import render
from .models import Product, Category

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

def auth(request):
    return render(request, 'auth.html')

def product(request):
    return render(request, 'product_page.html')
