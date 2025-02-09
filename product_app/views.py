from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import view_model,Brand,cetagory,country,colour,Team,MainMetariails,version,TypeOFJacket,range_of_price,Movement_Watch,size,Product,warenty
from .serializer import ViewSerializer
from man.serializer import CetagorySerializer,BrandSerializer,TypeOfJacketsSerializer,warentyes_serialzier
from .serializer import colorserializer,countryserializer,SizeSerializer,MovementSerializer,ProductSerializer
from sports.serializer import TeamSerializer,MainMaterialSerializer,versionSerailizer
from woman_app.serializer import reange_of_price_serializer
from rest_framework import permissions
class viewModelObject(APIView):
    
    def get(self,request,format=None):
        queryset = view_model.objects.filter(user=request.user)
        serilizaer = ViewSerializer(queryset,many=True)
        return Response(serilizaer.data)
    
class ViewMOdelapiview(APIView):
    
    def delete(self,request,pk,format=None):
        obj = view_model.objects.get(pk=pk)
        obj.delete()
        return Response('Recent Item Delete')
    
class DeliveryView(APIView):
    def post(self,request,format=None):
        serializer = DeliverySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def get(self,request,format=None):
        queryset = Delivery.objects.all()
        serializer = DeliverySerializer(queryset,many=True)
        return Response(serializer.data)





class BrandPost(APIView):
    
    def get(self,request,format=None):
        queryset = Brand.objects.all()
        serializer = BrandSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Brand post done')
        else:
            return Response(serializer.errors)
        
class CetagoryPost(APIView):
    
    def get(self,request,format=None):
        queryset = cetagory.objects.all()
        serializer = CetagorySerializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = CetagorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('ceta Post Done')
        
        
class CountryPost(APIView):
    
    def get(self,request,format=None):
        queryset = country.objects.all()
        seriaizer = countryserializer(queryset,many=True)
        return Response(seriaizer.data)
    
    def post(self,request,format=None):
        serializer = countryserializer(data=request.data)
        if country.objects.filter(country_name=request.data['country_name'] == True):
            return Response('Country Already exits')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
class CountryPUTDelete(APIView):
    
    def get(self,request,pk,format=None):
        obj = country.objects.get(pk=pk)
        serializer = countryserializer(obj)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        obj = country.objects.get(pk=pk)
        serializer = countryserializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('PUT Done Country')
        
    def delete(self,request,pk,format=None):
        obj = country.objects.get(pk=pk)
        obj.delete()
        return Response('Country Delete')

        
class ColourPost(APIView):
    
    def get(self,request,format=None):
        queryset = colour.objects.all()
        seriaizer = colorserializer(queryset,many=True)
        return Response(seriaizer.data)
    
    
    def post(self,request,format=None):
        serialzier = colorserializer(data=request.data)
        
    
        if colour.objects.filter(colour_name=request.data['colour_name']).exists():
            return Response('Already Exits')
        if serialzier.is_valid():
            serialzier.save()
            return Response('colour post done')

class SizePOst(APIView):
    
    def get(self,request,format=None):
        
        queryset = size.objects.all()
        serializer = SizeSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serailzer = SizeSerializer(data=request.data)
        if serailzer.is_valid():
            serailzer.save()
            return Response('size Done')
        
        
class DeletePUtColour(APIView):
    
    def delete(self,request,pk,format=None):
        obj = colour.objects.get(pk=pk)
        obj.delete()
        return Response('Colour Deleted')
    
    def put(self,request,pk,format=None):
        obj = colour.objects.get(pk=pk)
        seriaizer = colorserializer(obj,data=request.data)
        if seriaizer.is_valid():
            seriaizer.save()
            return Response('PUt done')
        
        
    def get(self,request,pk,format=None):
        obj = colour.objects.get(pk=pk)
        seriazlizer = colorserializer(obj)
        return Response(seriazlizer.data)
    
class BrandDeletePUT(APIView):
    
    def get(self,request,pk,format=None):
        
        obj = Brand.objects.get(pk=pk)
        serializer = BrandSerializer(obj)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        obj = Brand.objects.get(pk=pk)
        serializer = BrandSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk,format=None):
        
        obj = Brand.objects.get(pk=pk)
        obj.delete()
        return Response('Brand Item Delete')


class CetagoryPUTDelete(APIView):
    
    def get(self,request,pk,format=None):
        
        obj = cetagory.objects.get(pk=pk)
        serializer = CetagorySerializer(obj)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        obj = cetagory.objects.get(pk=pk)
        serializer = CetagorySerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('PUt done')
        
    def delete(self,request,pk,format=None):
        
        obj = cetagory.objects.get(pk=pk)
        obj.delete()
        return Response('Obj Delete Done!')
    
    
class AllTeam(APIView):
    
    
    def get(self,request,format=None):
        
        queryset = Team.objects.all()
        serializer = TeamSerializer(queryset,many=True)
        return Response(serializer.data)
    
    
    def post(self,request,format=None):
        
        serializer = TeamSerializer(data=request.data)
        if Team.objects.filter(name=request.data['name']):
            return Response('Already exits')
        
        if serializer.is_valid():
            serializer.save()
            return Response('Team POst done')
        
        return Response(serializer.error_messages)
    
    
class TeamNameDeleteAndPut(APIView):
    
    def get(self,request,pk,format=None):
        
        obj = Team.objects.get(pk=pk)
        serializer = TeamSerializer(obj)
        return Response(serializer.data)
    
    
    def delete(self,request,pk,format=None):
        obj = Team.objects.get(pk=pk)
        obj.delete()
        return Response('Team Name Deleted')
    
    
    def put(self,request,pk,format=None):
        obj = Team.objects.get(pk=pk)
        seriaizer = TeamSerializer(obj,data=request.data)
        if seriaizer.is_valid():
            seriaizer.save()
            return Response('Team name Put Done')
        
class MainMetarialsApiView(APIView):
    
    
    def get(self,request,format=None):
        obj = MainMetariails.objects.all()
        serializer = MainMaterialSerializer(obj,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = MainMaterialSerializer(data=request.data)
        if MainMetariails.objects.filter(name=request.data['name']):
            return Response('Already exits')
        if serializer.is_valid():
            serializer.save()
            return Response('Main Metarials Post Done')
        
        
class EditMetaDelete(APIView):
    
    
    def get(self,request,pk,format=None):
        
        obj = MainMetariails.objects.get(pk=pk)
        serializer = MainMaterialSerializer(obj)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        obj = MainMetariails.objects.get(pk=pk)
        seirliazer = MainMaterialSerializer(obj,data=request.data)
        if seirliazer.is_valid():
            seirliazer.save()
            return Response('put done')
        else:
            return Response(seirliazer.errors)
        
    def delete(self,request,pk,format=None):
        obj = MainMetariails.objects.get(pk=pk)
        obj.delete()
        return Response('Delet done')
    


class VersionPost(APIView):
    
    def get(self,request,format=None):
        obj = version.objects.all()
        serialzer = versionSerailizer(obj,many=True)
        return Response(serialzer.data)
    
    def post(self,request,format=None):
        sierlizer =versionSerailizer(data=request.data)
        if version.objects.filter(name=request.data['name']):
            return Response('Already Exits')
        
        if sierlizer.is_valid():
            sierlizer.save()
            return Response('Post done')
        else:
            return Response(sierlizer.errors)
        
class VersionPutDelete(APIView):
    
    def put(self,request,pk,format=None):
        obj = version.objects.get(pk=pk)
        serialier = versionSerailizer(obj,data=request.data)
        if serialier.is_valid():
            serialier.save()
            return Response('Put Done')
        else:
            return Response(serialier.errors)
    
    def get(self,request,pk,format=None):
        obj = version.objects.get(pk=pk)
        seiralizer = versionSerailizer(obj)
        return Response(seiralizer.data)
    
    def delete(self,request,pk,format=None):
        obj = version.objects.get(pk=pk)
        obj.delete()
        return Response('Delete done')
    
    
class TypeOfjaceketPost(APIView):
    def get(self,request,format=None):
        queryset = TypeOFJacket.objects.all()
        serializer = TypeOfJacketsSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        seirlalizer = TypeOfJacketsSerializer(data=request.data)
        if TypeOFJacket.objects.filter(name=request.data['name']):
            return Response('Already Exits')
        if seirlalizer.is_valid():
            seirlalizer.save()
            return Response('Type of jacket Post Done')
        return Response(seirlalizer.errors)


class JacketPutDelete(APIView):
    def get(self,request,pk,format=None):
        obj = TypeOFJacket.objects.get(pk=pk)
        serializer = TypeOfJacketsSerializer(obj)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        obj = TypeOFJacket.objects.get(pk=pk)
        serializer = TypeOfJacketsSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Put done')
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk,format=None):
        obj = TypeOFJacket.objects.get(pk=pk)
        obj.delete()
        return Response('Delete Done')
    
class RangePriceDeletePut(APIView):
    
    
    def put(self,request,pk,format=None):
        obj = range_of_price.objects.get(pk=pk)
        print(request.data)
        serializer = reange_of_price_serializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Put Done')
        
    def get(self,request,pk,format=None):
        obj = range_of_price.objects.get(pk=pk)
        serializer = reange_of_price_serializer(obj)
        return Response(serializer.data)
    
    def delete(self,request,pk,format=None):
        obj = range_of_price.objects.get(pk=pk)
        obj.delete()
        return Response('Delete Done')
    
    
class MoveMentWatchApi(APIView):
    
    
    def get(self,request,format=None):
        queryset = Movement_Watch.objects.all()
        seializer = MovementSerializer(queryset,many=True)
        return Response(seializer.data)
    
    def post(self,request,format=None):
        serilalzer = MovementSerializer(data=request.data)
        if Movement_Watch.objects.filter(title=request.data['title']):
            return Response("Already Exits")
        if serilalzer.is_valid():
            serilalzer.save()
            return Response('Post Done')
        

class MoveMentPutDelApivew(APIView):
    
    
    def put(self,request,pk,format=None):
        obj = Movement_Watch.objects.get(pk=pk)
        serializer = MovementSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Put Done')
        
    def delete(self,request,pk,format=None):
        obj = Movement_Watch.objects.get(pk=pk)
        obj.delete()
        return Response('Delete Done')
    
    
class SizeApiView(APIView):
    
    def get(self,request,format=None):
        obj  = size.objects.all()
        seralizer = SizeSerializer(obj,many=True)
        return Response(seralizer.data)
    
    def post(self,request,format=None):
        seriliazer = SizeSerializer(data=request.data)
        
        if size.objects.filter(size_name=request.data['size_name']):
            return Response('Already Exits')
        if seriliazer.is_valid():
            seriliazer.save()
            return Response('Post Done')
        return Response(seriliazer.errors)
    
class SizeUpdate(APIView):
    
    def put(self,request,pk,format=None):
        obj = size.objects.get(pk=pk)
        serializer = SizeSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Put done")
        else:
            return Response(serializer.errors)
        
    def get(self,request,pk,format=None):
        obj = size.objects.get(pk=pk)
        serializer = SizeSerializer(obj)
        return Response(serializer.data)
    
    
    def delete(self,request,pk,format=None):
        obj = size.objects.get(pk=pk)
        obj.delete()
        return Response("delet Done")




class ProductPostApiViw(APIView):
        def post(self,request,format=None):
            seirliazer = ProductSerializer(data=request.data)
            if seirliazer.is_valid():
                seirliazer.save()
                return Response('Post Done')
            else:
                return Response(seirliazer.errors)
            
            
        def get(self,request,format=None):
            obj = Product.objects.all()
            return Response(ProductSerializer(obj,many=True).data)
        
        
class WarrentyApiView(APIView):
    # permission_classes=[permissions.IsAuthenticated]
    
    def get(self,request,format=None):
        queryset = warenty.objects.all()
        serializer = warentyes_serialzier(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = warentyes_serialzier(data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response('Post Done')
        else:
            return Response(serializer.errors)
        
        
class WarrentyCrudApiview(APIView):
    
    def get(self,request,pk,format=None):
        obj = warenty.objects.get(pk=pk)
        serializer = warentyes_serialzier(obj)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        obj = warenty.objects.get(pk=pk)
        serializer = warentyes_serialzier(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('PUT DONE')
        else:
            return Response(serializer.errors)
        
        
        
    def delete(self,request,pk,format=None):
        obj = warenty.objects.get(pk=pk)
        obj.delete()
        return Response("Delete done")