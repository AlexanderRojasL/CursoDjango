from rest_framework import serializers
from .models import Product

# Un serializer para convertir un modelo a JSON y viceversa.
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
