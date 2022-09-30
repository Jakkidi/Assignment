from itertools import product
from rest_framework import serializers 
from .models import product,cart
class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'
class cartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart
        fields = '__all__'