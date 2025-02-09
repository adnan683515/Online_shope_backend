from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

# Create your models here.


class Register_serializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields =['id','username','first_name','last_name','email','password','confirm_password']
        
        
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        
        if password != confirm_password:
            return  serializers.ValidationError("Password Doesn't Match!")
        
        if User.objects.filter(email=email).exists():
            return serializers.ValidationError('This email Already Exits')
        
        user = User(username=username,first_name=first_name,last_name=last_name,email=email)
        user.set_password(password)
        user.is_active = False
        user.save()
        
        return user
        
    
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','is_staff'] 
            
class log_in_serializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
    
    
from django.contrib.auth.password_validation import validate_password

class PasswordChangeSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
    
    def validate(self,data):
        if data['new_password'] != data['confirm_password']:
            return serializers.ValidationError("new password and confirm password does not match!")
        validate_password(data['new_password'])  
        return data