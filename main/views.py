from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, ProductMaterial, Warehouses


class ProductAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        result = []
        for product in products:
            product_data = {
                'product_name': product.name,
                'product_qty': product.count,
                'product_materials': []
            }

            product_materials = ProductMaterial.objects.filter(product=product)

            for product_material in product_materials:
                warehouses = Warehouses.objects.filter(material=product_material.material).first()
                if warehouses:
                    d = {
                        'warehouse_id': warehouses.id,
                        'material_name': product_material.material.name,
                        'qty': product_material.quantity,
                        'price': warehouses.price
                    }
                    product_data['product_materials'].append(d)
            result.append(product_data)
        return Response({'result': result})