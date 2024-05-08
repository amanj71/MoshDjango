from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection, Customer

# write your serializers here
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('id', 'title', 'featured_product')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'slug', 'price', 'inventory', 'collection', 'price_with_tax')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return round(product.price*Decimal(1.1), 2)