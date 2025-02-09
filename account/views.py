from django.shortcuts import render,redirect
from rest_framework.views import APIView
from .serializer import Register_serializer,log_in_serializer,userSerializer,PasswordChangeSerializer
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework import status
# Create your views here.

class register_view(APIView):
    
    def post(self,request,format=None):
        serializer = Register_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            token= default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            
            confirm_link = f"http://127.0.0.1:8000/active/{uid}/{token}/"
            email_subject = "confirmation Email"
            
            email_body = render_to_string('email.html',{'confirm_email':confirm_link,'email_subject':email_subject})
            email = EmailMultiAlternatives(email_subject," ",to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            print("email send done")
            
            return Response("check Your Email")
        
        else:
            return Response(serializer.errors)
    
    def get(self,request,format=None):
        queryset = User.objects.all()
        serializer = userSerializer(queryset,many=True)
        return Response(serializer.data)
        
        
class userDetails(APIView):
    
    def get(self,request,pk,format=None):
        queryset = User.objects.get(pk=pk)
        print(queryset)
        serializer = userSerializer(queryset)
        return Response(serializer.data)
        
class log_in_view(APIView):
    
    def post(self,request):
        serializer = log_in_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']  
            user = authenticate(username=username,password=password)
            if user:
                token,_= Token.objects.get_or_create(user=user)
                login(request,user)
                return Response({'token':token.key,'user_id':user.pk},status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors)
        
        
def activate(request,uidb64,token):
    try :
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(user.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect('http://127.0.0.1:5500/login.html')
    else:
        return redirect('register')
    
class logoutView(APIView):
    def get(self,request):
        logout(request)
        return redirect('login')
        
class adminSaff(APIView):
    
    def get(self,request,pk,format=None):
        obj = User.objects.get(pk=pk)
        seriaizer = userSerializer(obj)
        return Response(seriaizer.data)


class passwordview(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,format=None):
        serializer = PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            new_pass = request.data['new_password']
            user.set_password(new_pass)
            user.save()
            return Response('done')
        else:
            return Response(serializer.errors)