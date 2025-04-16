from django.shortcuts import render

# Пример представления для главной страницы
def index(request):
    return render(request, 'main.html')

def catalog(request):
    return render(request, 'catalog.html')

def auth(request):
    return render(request, 'auth.html')

def product(request):
    return render(request, 'product_page.html')
