from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from product_app.models import Product
from rest_framework import viewsets
from .models import Order,Cart,CartItem
from .serializer import orderSerializer,CartItemSerializer,CartSerializer,CartItemSerializerPost,userSerailizer,OderSeriailzer

from django.template.loader import render_to_string
from django.core.mail import  EmailMultiAlternatives

class orderView(APIView):
    
    def get(self,request,format=None):
        queryset = Order.objects.all()
        serializer  = OderSeriailzer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = orderSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            obj.total_price = request.data['total_price']
            obj.save()
            return Response('Order Done')
        else:
            return Response(serializer.errors)
        
    def delete(self,request,format=None):
        oder_id_params = self.request.query_params.get('order_id_del')
        if oder_id_params:
            obj = Order.objects.get(pk=oder_id_params)
            obj.delete()
            return Response("Delete done")
        



class OderPut(APIView):
    
    def get(self,request,pk,format=None):
        obj = Order.objects.get(pk=pk)
        seriaizer = orderSerializer(obj)
        return Response(seriaizer.data)
    
    def put(self,request,pk,format=None):
        obj  = Order.objects.get(pk=pk)
        serializer = orderSerializer(obj,data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            obj.status = request.data['status']
            obj.save()
            if obj.status == 'Shipped':
                mail_sub = 'Hello Dear Customer!'
                email_body = render_to_string('status_email.html',{'mail_sub':mail_sub,"product":obj.product,'obj':obj})
                email = EmailMultiAlternatives(mail_sub,'',to=[obj.user.email])
                email.attach_alternative(email_body,'text/html')
                email.send()
            if obj.status == 'Delivered':
                mail_sub = 'Hello Dear Customer!'
                email_body = render_to_string('deliverd_email.html',{'mail_sub':mail_sub,"product":obj.product,'obj':obj})
                email = EmailMultiAlternatives(mail_sub,'',to=[obj.user.email])
                email.attach_alternative(email_body,'text/html')
                email.send()
            return Response('Put done')

class CartView(APIView):
    def get(self,request,format=None):
        quseryset = Cart.objects.all()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            obj = Cart.objects.get(user=user_id)
            serializer = CartSerializer(obj)
            return Response(serializer.data)
        
        serilaizer = CartSerializer(quseryset,many=True)
        return Response(serilaizer.data)
    
    def post(self,request,format=None):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            if Cart.objects.filter(user=request.user).count() > 0 :
                return Response('Already Cart Created')
            serializer.save()
            return Response('Cart Created')
        else:
            return Response(serializer.errors)
        
class CartItemsView(APIView):
    def get(self,request,format=None): 
        cart_id = self.request.query_params.get('cart_id')
        if cart_id:
            queryset = CartItem.objects.filter(cart=cart_id)
        serializer = CartItemSerializer(queryset,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer = CartItemSerializerPost(data=request.data)
        if serializer.is_valid():
            item = Product.objects.get(pk=request.data['product'])
            if item.quantity > 0:
                if CartItem.objects.filter(cart=request.data['cart'],product=request.data['product']):
                    obj = CartItem.objects.get(cart=request.data['cart'],product=request.data['product'])
                    obj.quantity += int(request.data['quantity'])
                    obj.price += int(request.data['quantity'])*int(item.fixed_price)
                    obj.save()
                    return Response('product updated')
                ans = serializer.save()
                ans.price = int(request.data['quantity'])*int(item.fixed_price)
                ans.save()
                return Response('Product Cart Added')
            else:
                return Response('Product Empty!')
        else:
            return Response(serializer.errors)
    
    
class CartItemsUpdate(APIView):
        def put(self, request, pk, format=None):
            obj = CartItem.objects.get(pk=pk)
            serializer = CartItemSerializerPost(obj, data=request.data)
            if serializer.is_valid():
                cartitem = CartItem.objects.get(pk=request.data['id'])
                product = Product.objects.get(pk=request.data['product'])
                cartitem.price += int(request.data['quantity'])*int(product.fixed_price)
                cartitem.quantity += request.data['quantity']
                cartitem.save()
    
            return Response("PUt done")

        
        def get(self,request,pk,format=None):
            obj = CartItem.objects.get(pk=pk)
            serializer = CartItemSerializer(obj)
            return Response(serializer.data)
        
        
        def delete(self,request,pk,format=None):
            obj = CartItem.objects.get(pk=pk)
            obj.delete()
            return Response("Delete Done")



class user_details(APIView):
    
    def get(self,request,pk,format=None):
        
        obj = User.objects.get(pk=pk)
        serializer = userSerailizer(obj)
        return Response(serializer.data)





from .serializer import OderSeriailzer


class OrderListapiView(APIView):
    
    def get(self,request,format=None):
        
        queryset = Order.objects.filter(user=request.user)

        oder_id = self.request.query_params.get('oderitem_id')
        if oder_id:
            obj = Order.objects.get(pk=oder_id)
            return Response(OderSeriailzer(obj).data)
        
        serializer = OderSeriailzer(queryset,many=True)
        return Response(serializer.data)




class FilterOderlist(APIView):
    
    def get(self,request,format=None):
        date_time = self.request.query_params.get('date_oder')
        end_date = self.request.query_params.get('end_date')
    
        queryset = Order.objects.all()
        if date_time:
            queryset = Order.objects.filter(oderdate__range=[date_time,end_date])
        
        serializer = OderSeriailzer(queryset,many=True)
        return Response(serializer.data)






























































