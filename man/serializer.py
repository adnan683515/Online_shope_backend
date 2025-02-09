
from rest_framework import serializers
from product_app.models import Product,review,size,Brand,country,favorites,TypeOFJacket,cetagory
from django.contrib.auth.models import User

from product_app.models import view_model,warenty
class userSerailzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name']

class size_fo_geans_serializer(serializers.ModelSerializer):
    class Meta:
        model = size
        fields = '__all__'
        

class CountrySerializer(serializers.ModelSerializer):
    model = country
    fields ='__all__'

class CetagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = cetagory
        fields = '__all__'


        
    

        
class review_serializer(serializers.ModelSerializer):
    class Meta:
        model = review
        exclude = ['football_rating']
        
class ReviewSerializerForGet(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    class Meta:
        model = review
        exclude = ['football_rating']
        

        
        
class FevSerializer(serializers.ModelSerializer):
    class Meta:
        model = favorites
        fields = '__all__'
    
class product_seriliazer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'    
        
        
class ViewProductSerializer(serializers.ModelSerializer):
    Product = product_seriliazer(read_only=True)
    class Meta:
        model = view_model
        fields = '__all__'
        
class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = view_model
        fields = '__all__'
            

class warentyes_serialzier(serializers.ModelSerializer):
    class Meta:
        model = warenty
        fields = '__all__'
        
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        
        
class jacketSerializer(serializers.ModelSerializer):
    Brand = BrandSerializer()
    cetagory = CetagorySerializer()
    class Meta:
        model = Product
        fields = ['id','cetagory','type_your_product','TypeOFJacket','Brand','product_title','display_image','font_image','quantity','range_of_price','fixed_price','colour','country','size','warenty','description','MainMetariails','abailable','eyes']
        

        
        
class TypeOfJacketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOFJacket
        fields = '__all__'
        
class geans_serializer(serializers.ModelSerializer):
    country = serializers.CharField(read_only=True)
    size = serializers.CharField(read_only=True)
    range_of_price = serializers.CharField(read_only=True)
    colour = serializers.CharField(read_only=True)
    Brand  = BrandSerializer()
    cetagory = CetagorySerializer()
    class Meta:
        model = Product
        fields = '__all__'



class WatchSerializer(serializers.ModelSerializer):
    country = serializers.CharField(read_only=True)
    Brand = BrandSerializer()
    cetagory = CetagorySerializer()
    colour = serializers.CharField(read_only=True)
    Dial_size_watch = serializers.CharField(read_only=True)
    range_of_price = serializers.CharField(read_only=True)
    warenty = serializers.CharField(read_only=True)
    Movement_Watch = serializers.CharField(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        
class ShirtSerializer(serializers.ModelSerializer):
    country = serializers.CharField(read_only=True)
    Brand = BrandSerializer()
    colour = serializers.CharField(read_only=True)
    class Meta:
        model = Product
        exclude = '__all__'
