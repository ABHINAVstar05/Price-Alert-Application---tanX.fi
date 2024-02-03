# This .py file contains api_views for alert creation, deletion and fetching users' alert records as per need.

"""
This file has 2 api_views namely,

1.) create --> this is used to create new alerts for a user and accepts only POST requests.
2.) delete --> this is used to delete alerts for a user and accepts only DELETE requests.
3.) fetch --> this is used to fetch a user's alert records as per need and accepts only POST requests.

"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, AlertSerializer
from .models import *

# API endpoint to create alert.

@api_view(['POST', ])
def create(request) :
    data = request.data

    username = data['username']
    try :
        user = User.objects.get(username = username)
        data['username'] = user.id
    except User.DoesNotExist :
        return Response({'Message': 'User does not exist.'})

    deserialized = AlertSerializer(data = data)

    if deserialized.is_valid() :
        deserialized.save()
        return Response({
            'Message' : 'Alert created successfully.',
            'Details': {
                'username': username,
                'alert_purpose': deserialized.data['alert_purpose'],
                'alert_price': deserialized.data['alert_price'],
                'alert_status': deserialized.data['alert_status']}
            })
    
    else :
        return Response(deserialized.errors)
    

# API endpoint to delete alert.
    
@api_view(['DELETE', ])
def delete(request) :
    data = request.data

    username = data['username']
    try :
        user = User.objects.get(username = username)
        data['username'] = user.id
    except User.DoesNotExist :
        return Response({'Message': 'User does not exist.'})

    try :
        alert = Alert.objects.get(username = data['username'], alert_purpose = data['alert_purpose'])
        alert.delete()
        return Response({
            'Message' : 'Alert with below details deleted successfully.',
            'Details': {
                'username': username,
                'alert_purpose': data['alert_purpose']
                }
            })

    except Alert.DoesNotExist :
        return Response({'Message': 'No such alert exists.'})


# API endpoint to fetch user's alert records.

@api_view(['POST', ])  # user needs to enter username and other optional data to fetch his/her alerts. 
def fetch(request) :
    data = request.data

    username = data['username']
    alert_status = data.get('alert_status', None)
    
    try :
        user = User.objects.get(username = username)
        data['username'] = user.id
    except User.DoesNotExist :
        return Response({'Message': 'User does not exist.'})

    if alert_status is not None :
        alert = Alert.objects.filter(username = data['username'], alert_status = alert_status)
    else :
        alert = Alert.objects.filter(username = data['username'])

    serializer = AlertSerializer(alert, many = True)
    return Response({'username': username, 'alert details': serializer.data})
    