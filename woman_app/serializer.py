from rest_framework import serializers
from product_app.models import Product,review,range_of_price,view_model,cetagory,colour,range_of_price
from man.serializer import BrandSerializer,CetagorySerializer

class colour_serializer(serializers.ModelSerializer):
    class Meta:
        model = colour
        fields = '__all__'

class saree_serializer(serializers.ModelSerializer):
    country = serializers.CharField(read_only=True)
    cetagory = serializers.CharField(read_only=True)
    Brand  = BrandSerializer()
    cetagory = CetagorySerializer()
    class Meta:
        model = Product
        exclude = ['size']
        

        
class saree_review_serializer(serializers.ModelSerializer):
    Product = saree_serializer(read_only=True)
    class Meta:
        model = review
        exclude = ['football_rating']
        

class view_serializer(serializers.ModelSerializer):
    class Meta:
        model = view_model
        fields = '__all__'
        
        

class cetagory_serializer(serializers.ModelSerializer):
    class Meta:
        model = cetagory
        fields = '__all__'
        

class reange_of_price_serializer(serializers.ModelSerializer):
    class Meta:
        model = range_of_price
        fields = '__all__'
    
