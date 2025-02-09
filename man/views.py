from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from product_app.models import Product,review,size,Brand,favorites,TypeOFJacket,cetagory
from .serializer import geans_serializer,review_serializer,size_fo_geans_serializer,ShirtSerializer,ReviewSerializerForGet,FevSerializer,ViewProductSerializer,ViewSerializer,jacketSerializer,TypeOfJacketsSerializer,BrandSerializer
from rest_framework import status
from django.http import Http404
from product_app.models import view_model
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from woman_app.serializer import cetagory_serializer
# Create your views here.
class BrandGeansView(APIView):
    def get(self,request,format=None):
        queryset = Brand.objects.filter(choice='geans')

        serializer = BrandSerializer(queryset,many=True)
        
        return Response(serializer.data)
    
class CetagoryGeansView(APIView):
    def get(self,request,format=None):
        queryset = cetagory.objects.filter(cetagorytype='Geans')
        serializer = cetagory_serializer(queryset,many=True)
        
        return Response(serializer.data)

class geans_list_post(APIView):
    
    def get(self,request,format=None):
        queryset = Product.objects.filter(type_your_product='Geans')
        
        geans_id = self.request.query_params.get('geans_cetagory_id')
        if geans_id:
            queryset = Product.objects.filter(cetagory=geans_id)
        
        colour_id = self.request.query_params.get('colour_id')
        if colour_id:
            queryset = Product.objects.filter(colour=colour_id,type_your_product='Geans')
        
        brand_id = self.request.query_params.get("brand_id")
        if brand_id:
            queryset = Product.objects.filter(Brand=brand_id,type_your_product='Geans')
            
        size_id = self.request.query_params.get('size_id')
        if size_id:
            queryset = Product.objects.filter(size=size_id,type_your_product='Geans')
            
        tk_id = self.request.query_params.get('taka_id')
        if tk_id:
            queryset = Product.objects.filter(range_of_price=tk_id,type_your_product='Geans')
            
        product_title = self.request.query_params.get('title')
        if product_title:
            queryset = Product.objects.filter(product_title=product_title,type_your_product='Geans')
        serializer = geans_serializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = geans_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)




class details_geans_or_put_delete(APIView):
    permissions = [permissions.IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            
            raise Http404

    def get(self, request, pk, format=None):
            queryset = Product.objects.get(pk=pk)
            ans  = view_model.objects.all()
            
            if len(ans) != 0:
                if  view_model.objects.filter(Product=pk,user=request.user).exists() !=True:
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
    
            serializer = geans_serializer(queryset)
            return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = geans_serializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response('Geans product Deleted!')
    
    
    
class RecentViewDeleteApiview(APIView):
    
    def get(self,request,pk,format=None):
        obj = view_model.objects.get(pk=pk)
        serializer = ViewSerializer(obj)
        return Response(serializer.data)
    
    def delete(self,request,pk,format=None):
        obj = view_model.objects.get(pk=pk)
        obj.delete()
        return Response("Delete Success")

class review_viewset(viewsets.ModelViewSet):
    queryset = review.objects.all()
    serializer_class = review_serializer
    # serializer_class = ReviewSerializerForGet
    
    
    def get_queryset(self):
        queryset =  super().get_queryset()
        
        product_id = self.request.query_params.get("product_id")
        if product_id:
            queryset = review.objects.filter(Product=product_id)
        return queryset
    

class ReviewForGetview(APIView):
    
    
    def get(self,request,format=None):
        product_id = self.request.query_params.get("product_id")
        if product_id:
            queryset = review.objects.filter(Product=product_id)
            serializer = ReviewSerializerForGet(queryset,many=True)
            return Response(serializer.data)
            
    

class SizeOfGeansView(APIView):
    
    def get(self,request,format=None):
        queryset = size.objects.filter(choice_size='Geans')
        serializer = SizeSerializer(queryset,many=True)
        return Response(serializer.data)
    
    
class ShirtListView(APIView):

    def get(self,request,format=None):
        queryset = Product.objects.filter(type_your_product='Shirt')
        
        Brand_id = self.request.query_params.get('brand_id')
        if Brand_id:
            queryset = Product.objects.filter(Brand=Brand_id,type_your_product='Shirt')
            
        tk_id = self.request.query_params.get('tk_id')
        if tk_id:
            queryset = Product.objects.filter(range_of_price=tk_id,type_your_product='Shirt')
            
        colour_id = self.request.query_params.get('colour_id')
        if colour_id:
            queryset = Product.objects.filter(colour=colour_id,type_your_product='Shirt')
            
        cetagory_id = self.request.query_params.get('ceta_id')
        if cetagory_id:
            queryset = Product.objects.filter(type_your_product='Shirt',cetagory=cetagory_id)
        serializer = ShirtSerializer(queryset,many=True)
        return Response(serializer.data)
    
    
class BrandShirtView(APIView):
    
    def get(self,request,format=None):
        queryset = Brand.objects.filter(choice='Shirt')
        serializer = BrandSerializer(queryset,many=True)
        return Response(serializer.data)
    
    
class ShirtCetagoryView(APIView):
    
    def get(self,request,format=None):
        queryset = cetagory.objects.filter(cetagorytype='Shirt')
        serializer = cetagory_serializer(queryset,many=True)
        return Response(serializer.data)
    
    
class FavView(APIView):
    
    def get(self,request,format=None):
        queryset = favorites.objects.filter(user=request.user)
        serializer = FevSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = FevSerializer(data=request.data)
        
        if serializer.is_valid():
            if favorites.objects.filter(user=request.user,Product=request.data['Product']).exists():
                return Response('This Product is Already Exits in Fav model')
            serializer.save()
            return Response('Favourites Done!')
        else:
            return Response(serializer.errors)
        



class ShirtDetailsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
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
                
            serializer = ShirtSerializer(queryset)
            return Response(serializer.data)
        
        
class ViewproductApiview(viewsets.ModelViewSet):
    queryset = view_model.objects.all()
    serializer_class = ViewProductSerializer
    
    def get_queryset(self):
        queryset  =  super().get_queryset()

        queryset = view_model.objects.filter(user=self.request.user)
        
        return queryset
    
    
    
    
    
####################  Watches  #############################
from .serializer import warentyes_serialzier,WatchSerializer,CetagorySerializer
from product_app.models import warenty,MainMetariails
from product_app.serializer import SizeSerializer,MainmetariailsSerializer

class WatchCetagoryView(APIView):
    
    def get(self,request,format=None):
        queryset = cetagory.objects.filter(cetagorytype='Watch')
        serializer = CetagorySerializer(queryset,many=True)
        return Response(serializer.data)
    
    
    def post(self,request,format=None):
        seriailzer = cetagory_serializer(data=request.data)
        
        if seriailzer.is_valid():
            seriailzer.save()
            return Response("Post Done")
        return Response(seriailzer.errors)
    
    
class BrandWatchView(APIView):
    
    def get(self,request,format=None):
        queryset = Brand.objects.filter(choice='Watch')
        serializer  = BrandSerializer(queryset,many=True)
        return Response(serializer.data)
    
    
class WarentyView(APIView):
    
    def get(self,request,format=None):
        queyset = warenty.objects.all()
        serializer = warentyes_serialzier(queyset,many=True)
        return Response(serializer.data)
    

class DiyalSizeview(APIView):
    
    def get(self,request,format=None):
        queryset = size.objects.filter(choice_size='Watch')
        serilizer = SizeSerializer(queryset,many=True)
        return Response(serilizer.data)
    
    
class StrapMetarailview(APIView):
    
    def get(self,request,format=None):
        queryset = MainMetariails.objects.filter(choice_option='watch')
        serilaizer = MainmetariailsSerializer(queryset,many=True)
        return Response(serilaizer.data)
    
class WatchProductView(APIView):
    
    def get(self,request,format=None):
        queryset = Product.objects.filter(type_your_product='Watch')
        
        cetagory_id = self.request.query_params.get('cetagory_id')
        if cetagory_id:
            queryset = Product.objects.filter(type_your_product='Watch',cetagory=cetagory_id)
            
            
        brand_watch = self.request.query_params.get('brand_id')
        if brand_watch:
            queryset = Product.objects.filter(type_your_product='Watch',Brand=brand_watch)
        
        strap_id = self.request.query_params.get('strap_id')
        if strap_id:
            queryset = Product.objects.filter(type_your_product='Watch',MainMetariails=strap_id)
            
            
        warenty_id = self.request.query_params.get('warenty_id')
        if warenty_id:
            queryset = Product.objects.filter(type_your_product='Watch',warenty=warenty_id)
            
        diyal_size = self.request.query_params.get('diyal_size_id')
        if diyal_size:
            queryset = Product.objects.filter(type_your_product='Watch',size=diyal_size)
            
        tk_id = self.request.query_params.get('tk_id')
        
        if tk_id:
            queryset = Product.objects.filter(type_your_product='Watch',range_of_price=tk_id)
        serializer = WatchSerializer(queryset,many=True)
        return Response(serializer.data)
    
    
    
class WatchDetailsView(APIView):
    
    def get(self,request,pk,format=None):
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
        serilazer = WatchSerializer(queryset)
        return Response(serilazer.data)
    
    
class ManJacketView(APIView):
    
    def get(self,request,format=None):
        queryset = Product.objects.filter(type_your_product='Jacket')
        product_id = self.request.query_params.get('product_id')
        
        brand_id = self.request.query_params.get('brand_id')
        if brand_id:
            queryset = Product.objects.filter(type_your_product="Jacket",Brand=brand_id)
        
        warrenty_id = self.request.query_params.get('warrenty_id')
        if warrenty_id:
            queryset = Product.objects.filter(type_your_product="Jacket",warenty=warrenty_id)
            
        colour_id = self.request.query_params.get('colour_id')
        if colour_id:
            queryset = Product.objects.filter(type_your_product='Jacket',colour=colour_id)
            
        type_jac_id = self.request.query_params.get('type_jac_id')
        if type_jac_id:
            queryset = Product.objects.filter(type_your_product='Jacket',TypeOFJacket=type_jac_id)
        if product_id:
            item = Product.objects.get(pk=product_id)
            
            queryset = Product.objects.filter(type_your_product='Jacket',Brand=item.Brand)
            serializer = jacketSerializer(queryset,many=True)
                
            
        serialzer = jacketSerializer(queryset,many=True)
        return Response(serialzer.data)

class BrandJacketView(APIView):
    
    def get(self,request,format=None):
        quseryset = Brand.objects.filter(choice='jacket')
        serializer = BrandSerializer(quseryset,many=True)
        return Response(serializer.data)
        
class TypeOfJacketView(APIView):
    
    def get(self,request,format=None):
        queryset = TypeOFJacket.objects.all()
        seriailzer = TypeOfJacketsSerializer(queryset,many=True)
        return Response(seriailzer.data)
    
    
from .serializer import warentyes_serialzier

class JacksWarrentyView(APIView):
    
    def get(self,request,format=None):
        queryset = warenty.objects.filter(choice_type='jacket')
        serializer = warentyes_serialzier(queryset,many=True)
        return Response(serializer.data)

class JackDetailsView(APIView):
    
    def get(self,request,pk,format=None):
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
                
        serializer = jacketSerializer(queryset)
        return Response(serializer.data)
        