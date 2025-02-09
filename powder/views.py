from django.shortcuts import render
from rest_framework.views import APIView
from product_app.models import Product,review,view_model
from rest_framework.response import Response
from .serializer import powder_serializer,powder_review_serializer
from rest_framework import status
from rest_framework import viewsets
# Create your views here.
class powder_views(APIView):
    
    def post(self,request,format=None):
        serializer = powder_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
    
    def get(self, request, format=None):
        queryset = Product.objects.all()
        powder_id = self.request.query_params.get('powder_id')
        if powder_id:
            queryset = Product.objects.filter(powder_cetagory=powder_id)
            
        serializer = powder_serializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_410_GONE)
    
class powder_viewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = powder_serializer
        
    
    def get_queryset(self):
        queryset =  super().get_queryset()
        
        powder_id = self.request.query_params.get('powder_id')
        if powder_id:
            queryset = Product.objects.filter(powder_cetagory=powder_id)
            
        
        return queryset
    


class powder_review_viewset(viewsets.ModelViewSet):
    queryset = review.objects.all()
    serializer_class = powder_review_serializer
    
    def get_queryset(self):
        queryset =  super().get_queryset()
        
        Product_Id = self.request.query_params.get('product_id') 
        if Product_Id:
            queryset = review.objects.filter(Product=Product_Id)
        return queryset
    
            
class details_powder_or_put_delete(APIView):
    
    
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response("Product doesn't exits")

    def get(self, request, pk, format=None):
            queryset = Product.objects.get(pk=pk)
            ans  = view_model.objects.all()
            print("ans ",ans)
            if len(ans) != 0:
                if view_model.objects.filter(Product=pk).exists() == False:
                    obj = view_model(Product=queryset,user=request.user,view=True)
                    obj.save()
            else:
                obj = view_model(Product=queryset,user=request.user,view=True)
                obj.save()
            serializer = powder_serializer(queryset)
            return Response(serializer.data)
        
    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = powder_serializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response('saree product Deleted!')
        
