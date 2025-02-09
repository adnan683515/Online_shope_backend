from django.shortcuts import render
from rest_framework import viewsets,views
from .serializer import football_serializer,review_football_serializer,TeamSerializer,JurseySerializer,versionSerailizer,CricketProductSerializer,MainMaterialSerializer,FootballSerializer,JurseySerializer
from product_app.models import Product,review,Team,version,MainMetariails,view_model,Brand,size
from rest_framework.views import APIView
from rest_framework.response import Response
from man.serializer import BrandSerializer,CetagorySerializer
from product_app.serializer import SizeSerializer

# Create your views here.

class VersionView(APIView):
    def get(self,request,format=None):
        queryset = version.objects.all()
        serializer = versionSerailizer(queryset,many=True)
        return Response(serializer.data)
    
class AllFootballsJust(APIView):
    
    def get(self,request,format=None):
        queryset = Product.objects.filter(type_your_product='Sports',sports_Type='Football')
        serializer = FootballSerializer(queryset,many=True)
        return Response(serializer.data)

class football_view(APIView):

    def get(self,request,format=None):
        queryset = Product.objects.filter(type_your_product='Sports')
        
        team_id = self.request.query_params.get('team_id')
        if team_id:
            queryset = Product.objects.filter(team=team_id,type_your_product='Sports',sports_Type='Jursi')
            return Response(JurseySerializer(queryset,many=True).data)
        
        version_id = self.request.query_params.get('version_id')
        if version_id:
            queryset = Product.objects.filter(version=version_id,type_your_product='Sports',sports_Type='Jursi')
            return Response(JurseySerializer(queryset,many=True).data)
        
        tk_id = self.request.query_params.get('tk_id')
        if tk_id:
            queryset = Product.objects.filter(range_of_price=tk_id,type_your_product='Sports',sports_Type='Jursi')
            return Response(JurseySerializer(queryset,many=True).data)
        
        colour_id = self.request.query_params.get('colour_Id')
        if colour_id:
            queryset = Product.objects.filter(colour=colour_id,type_your_product='Sports',sports_Type='Football')
            return Response(football_serializer(queryset,many=True).data)
        
        size_id = self.request.query_params.get('size_id')
        if size_id:
            queryset = Product.objects.filter(BatSize=size_id,type_your_product='Sports',sports_Type='Cricket Bat')
            return Response(CricketProductSerializer(queryset,many=True).data)
        
        
        cricket_brand = self.request.query_params.get('cricket_brand')
        if cricket_brand:
            queryset = Product.objects.filter(type_your_product='Sports',Brand=cricket_brand,sports_Type='Cricket Bat')
            return Response(CricketProductSerializer(queryset,many=True).data)
        
        metarial_id  = self.request.query_params.get('metarail_id')
        if metarial_id:
            queryset = Product.objects.filter(type_your_product='Sports',MainMetariails=metarial_id,sports_Type='Cricket Bat')
            return Response(CricketProductSerializer(queryset,many=True).data)
        
        price_id_football = self.request.query_params.get('price_fb')
        warenty_fb = self.request.query_params.get('warrenty_fb')
        
        if price_id_football or warenty_fb:
            queryset = Product.objects.filter(type_your_product='Sports',range_of_price=price_id_football,sports_Type='Football')
            return Response(FootballSerializer(queryset,many=True).data)
        
        serializer = football_serializer(queryset,many=True)
        return Response(serializer.data)

    
    
class SportSdetailis(APIView):
    def get(self,request,pk,format=None):
        Obj = Product.objects.get(pk=pk)
        if Obj.sports_Type=='Football':
            ans  = view_model.objects.all()
        
            if len(ans) != 0:
                if view_model.objects.filter(Product=pk,user=request.user).exists() == False:
                        
                    obj = view_model(Product=Obj,user=request.user,view=True)
                    obj.save()
                    eyes_obj = Product.objects.get(pk=pk)
                    eyes_obj.eyes += 1
                    eyes_obj.save()
                        
            else:
                obj = view_model(Product=Obj,user=request.user,view=True)
                obj.save()
                eyes_obj = Product.objects.get(pk=pk)
                eyes_obj.eyes += 1
                eyes_obj.save()
            return Response(FootballSerializer(Obj).data)
            
        if Obj.sports_Type == 'Cricket Bat':
            ans  = view_model.objects.all()
        
            if len(ans) != 0:
                if view_model.objects.filter(Product=pk,user=request.user).exists() == False:
                        
                    obj = view_model(Product=Obj,user=request.user,view=True)
                    obj.save()
                    eyes_obj = Product.objects.get(pk=pk)
                    eyes_obj.eyes += 1
                    eyes_obj.save()
                        
            else:
                obj = view_model(Product=Obj,user=request.user,view=True)
                obj.save()
                eyes_obj = Product.objects.get(pk=pk)
                eyes_obj.eyes += 1
                eyes_obj.save()
            return Response(CricketProductSerializer(Obj).data)   
        
        if Obj.sports_Type == 'Jursi':
            ans  = view_model.objects.all()
        
            if len(ans) != 0:
                if view_model.objects.filter(Product=pk,user=request.user).exists() == False:
                        
                    obj = view_model(Product=Obj,user=request.user,view=True)
                    obj.save()
                    eyes_obj = Product.objects.get(pk=pk)
                    eyes_obj.eyes += 1
                    eyes_obj.save()
                        
            else:
                obj = view_model(Product=Obj,user=request.user,view=True)
                obj.save()
                eyes_obj = Product.objects.get(pk=pk)
                eyes_obj.eyes += 1
                eyes_obj.save()
            return Response(JurseySerializer(Obj).data)
        
        return Response('Not data')

    
class MainMetarailView(APIView):
    
    def get(self,request,format=None):
        queryset = MainMetariails.objects.all()
        serializer = MainMaterialSerializer(queryset,many=True)
        return Response(serializer.data)
    
class TeamView(APIView):
    
    def get(self,request,format=None):
        queryset  = Team.objects.all()
        seriaizer = TeamSerializer(queryset,many=True)
        return Response(seriaizer.data)

class BatSizeView(APIView):
    
    def get(self,request,format=None):
        queryset = size.objects.filter(choice_size='Bat Size')
        serializer = SizeSerializer(queryset,many=True)
        return Response(serializer.data)

        
    
class review_viewset(viewsets.ModelViewSet):
    queryset = review.objects.all()
    serializer_class = review_football_serializer
    
    def get_queryset(self):
        queryset =  super().get_queryset()
    
        Product_Id = self.request.query_params.get('product_id')
        
        if Product_Id:
            queryset = review.objects.filter(Product=Product_Id)
            
        return queryset
    
    
class CricketBrandView(APIView):
    
    def get(self,request,format=None):
        queyset = Brand.objects.filter(choice='Cricket Bat')
        serializer = BrandSerializer(queyset,many=True)
        return Response(serializer.data)
    
    
class AllJurseyView(APIView):
    
    def get(self,request,format=None):
        queryset = Product.objects.filter(type_your_product='Sports',sports_Type='Jursi')
        serializer = JurseySerializer(queryset,many=True)
        return Response(serializer.data)