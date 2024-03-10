from rest_framework import serializers
from .models import Product, Material, ProductMaterial, Warehouses

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['name']

class ProductMaterialSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()

    class Meta:
        model = ProductMaterial
        fields = ['material', 'quantity']

class ProductSerializer(serializers.ModelSerializer):
    product_materials = ProductMaterialSerializer(many=True)

    class Meta:
        model = Product
        fields = ['name', 'product_materials']

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouses
        fields = ['id', 'material', 'remainder', 'price']