
from rest_framework import serializers
from product_app.models import Product
from django.contrib.auth.models import User
from .models import Cart,CartItem,Order
from product_app.serializer import ProductSerializer
from account.serializer import userSerializer

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
        
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = '__all__'
        
class CartItemSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

        
class orderSerializer(serializers.ModelSerializer):
    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    total_price = serializers.CharField(read_only=True)
    
    class Meta:
        model = Order
        fields = "__all__"
        


class userSerailizer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email']
        
        
class OderSeriailzer(serializers.ModelSerializer):
    user  = userSerailizer()
    product = ProductSerializer()
    class Meta:
        model = Order
        fields = '__all__'