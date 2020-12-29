from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Order(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=200)
    price = models.CharField(max_length=200)


class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
