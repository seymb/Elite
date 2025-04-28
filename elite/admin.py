from django.contrib import admin
from .models import Product, Category, Product_Price

class ProductPriceInline(admin.TabularInline):
    model = Product_Price
    extra = 1  # Количество пустых форм для добавления новых цен

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # Поля, которые будут отображаться в списке товаров
    inlines = [ProductPriceInline]  # Вставка формы для цен прямо в карточке товара

class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'volume', 'price', 'discount')  # Поля, которые будут отображаться для цен

admin.site.register(Product, ProductAdmin)
admin.site.register(Product_Price, ProductPriceAdmin)
admin.site.register(Category)