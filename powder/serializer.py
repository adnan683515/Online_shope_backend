

from product_app.models import Product,review
from rest_framework import serializers

class powder_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['size_of_geans']
    

class powder_review_serializer(serializers.ModelSerializer):
    class Meta:
        model = review
        exclude = ['football_rating']