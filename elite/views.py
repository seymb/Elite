from django.shortcuts import render

# Пример представления для главной страницы
def index(request):
    return render(request, 'main.html')