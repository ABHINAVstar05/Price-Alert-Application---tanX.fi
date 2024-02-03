# This .py file contains api_views for user authentication using JWT tokens.

"""
This file has 2 api_views namely,

1.) signup --> this is used for user registration and accepts only POST requests.
2.) login --> this is used for user authentication using JWT tokens to validate the users.

"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from .serializers import *

# signup api_view

@api_view(['POST', ])
def signup(request) :
    data = request.data
    deserialized = UserSerializer(data = data)

    if deserialized.is_valid() :
        deserialized.validated_data['password'] = make_password(deserialized.validated_data['password'])
        deserialized.save()
        return Response({'Message' : f'User created successfully.', 'User details' : [deserialized.data['username'], deserialized.data['email']] })
    
    else :
        return Response(deserialized.errors)
    

# signup api_view
    
@api_view(['POST', ])
def login(request) :
    data = request.data
    deserialized = LoginSerializer(data = data)

    if deserialized.is_valid() :
        username = deserialized.data['username']
        password = deserialized.data['password']

        if User.objects.filter(username = username) :
            user = User.objects.get(username = username)
            stored_password = user.password
            
            if(check_password(password, stored_password)) :
                refresh = RefreshToken.for_user(user)
                return Response({
                    'status': 200,
                    'message': 'OK',
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            
            else :
                return Response({
                    'status': 403,
                    'message': 'Invalid password.',
                    'data': {}
                })

        else :
            return Response({
                'status': 403,
                'message': 'User does not exist.',
                'data': {}
            })
        
    else :
        return Response({
            'status': 403,
            'message': 'Something went wrong.',
            'data': deserialized.errors
        })
    