from django.shortcuts import render

# Пример представления для главной страницы
def index(request):
    return render(request, 'main.html')
def men_page(request):
    return render(request, 'women_perf.html')
