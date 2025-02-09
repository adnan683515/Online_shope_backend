
from rest_framework import serializers
from rest_framework.response import Response
from .models import Product,view_model,country,colour,size,MainMetariails,Movement_Watch
class MainmetariailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainMetariails
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class ViewSerializer(serializers.ModelSerializer):
    Product = ProductSerializer()
    class Meta:
        model = view_model
        fields = '__all__'
        
class countryserializer(serializers.ModelSerializer):
    
    class Meta:
        model  = country
        fields = '__all__'
        
class colorserializer(serializers.ModelSerializer):
    
    class Meta:
        model  = colour
        fields = '__all__'
        
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = size
        fields = '__all__'

class MovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement_Watch
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields ='__all__'