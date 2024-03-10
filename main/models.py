from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    count = models.IntegerField()

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product

class Warehouses(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, null=True, blank=True)
    remainder = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return str(self.material)