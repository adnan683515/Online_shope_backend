from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .serializer import saree_serializer,saree_review_serializer,view_serializer,cetagory_serializer,colour_serializer,reange_of_price_serializer
from product_app.models import Product,review,view_model,cetagory,colour,range_of_price,Brand
from rest_framework.response import Response
from rest_framework import status
from man.serializer import BrandSerializer
from rest_framework.status import HTTP_404_NOT_FOUND
from django.http import Http404
from product_app.models import cetagory
# Create your views here.


class saree_api_view(APIView):
    
    def post(self,request,format=None):
        serializer = saree_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        
    
        queryset = Product.objects.filter(type_your_product='Saree')
        
        saree_id = self.request.query_params.get('saree_id')
        if saree_id:
            queryset = Product.objects.filter(cetagory=saree_id)
        
        title = self.request.query_params.get('product_title')
 
        if title:
            queryset = Product.objects.filter(product_title=title)
        
        range_of_price = self.request.query_params.get('range_of_price')
        if range_of_price:
            queryset = Product.objects.filter(range_of_price=range_of_price)
            
        brand_saree  = self.request.query_params.get("brand_saree")
        if brand_saree:
            queryset = Product.objects.filter(Brand_saree=brand_saree)
        cetagory = self.request.query_params.get('cetagory')
        print("Saree cetagory",cetagory)
        if cetagory:
            queryset = Product.objects.filter(cetagory=cetagory)
            
        colour_id = self.request.query_params.get('colour_id')
        if colour_id:
            queryset = Product.objects.filter(colour=colour_id,type_your_product='Saree')
            
            
    
        serializer = saree_serializer(queryset, many=True)
        
        return Response(serializer.data)
    
    
class view_saree(APIView):

    def get(self, request, format=None):
        
        saree_id = self.request.query_params.get('saree_id')
        if saree_id:
            queryset = view_model.objects.filter(Product=saree_id,view=True)
            serializer = view_serializer(queryset, many=True)
        
            return Response(serializer.data)


class details_saree_or_put_delete(APIView):
    
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            
            raise Http404

    def get(self, request, pk, format=None):
    
            queryset = Product.objects.get(pk=pk)
            
            ans  = view_model.objects.all()
        
            if len(ans) != 0:
                if view_model.objects.filter(Product=pk,user=request.user).exists() == False:
                    obj = view_model(Product=queryset,user=request.user,view=True)
                    obj.save()
                    eyes_obj = Product.objects.get(pk=pk)
                    eyes_obj.eyes += 1
                    eyes_obj.save()
            else:
                obj = view_model(Product=queryset,user=request.user,view=True)
                obj.save()
                eyes_obj = Product.objects.get(pk=pk)
                eyes_obj.eyes += 1
                eyes_obj.save()
                
            serializer = saree_serializer(queryset)
            return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = saree_serializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response('saree product Deleted!')

class saree_list_api_view(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = saree_serializer
    
class saree_review_list_api_view(ListAPIView):
    queryset = review.objects.all()
    serializer_class = saree_review_serializer
    
    

class saree_cetagory_api_view(APIView):
    
    def get(self,request,format=None):
        queryset = cetagory.objects.filter(cetagorytype='Saree')
        serializer = cetagory_serializer(queryset,many=True)
        return Response(serializer.data)
    
class colour_api_view(APIView):
    
    def get(self,request,format=None):
        
        queryset = colour.objects.all()
        serializer = colour_serializer(queryset,many=True)
        return Response(serializer.data)
    
    
class range_of_price_view(APIView):
    
    def get(self,request,format=None):
        
        queryset = range_of_price.objects.all()
        serializer = reange_of_price_serializer(queryset,many=True)
        
        return Response(serializer.data)
    
    def post(self,request,format=None):
        seriailzer = reange_of_price_serializer(data=request.data)
        if seriailzer.is_valid():
            seriailzer.save()
            return Response("POST DONE")
    
    
class brand_saree_view(APIView):
    
    def get(self,request,format=None):
        queryset = Brand.objects.filter(choice='Saree')
        serializer = BrandSerializer(queryset,many=True)
        
        return Response(serializer.data)