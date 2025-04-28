from django.db import models

class Admin(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Admin'


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Category'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, models.SET_NULL, db_column='category_ID', blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=False)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=False)
    stock = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'Product'

    def __str__(self):
        return self.name
    
class Product_Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    volume = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'Product_Price'


    def __str__(self):
        return f'{self.volume} мл - {self.price} P'
