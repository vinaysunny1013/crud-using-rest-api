from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status 
from .serializers import UserSerializer 
from .models import User 


@api_view(['GET'])
def get_users(req):
    users= User.objects.all()
    serializer=UserSerializer(users, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['POST'])
def create_user(req):
    # request.data
    serializer=UserSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data ,status=status.HTTP_201_CREATED) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT','DELETE','GET'])
def user_detail(req,pk):
    try:
        user=User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if req.method=='GET':
        serializer=UserSerializer(user)
        return Response(serializer.data)
    

    if req.method=="PUT":
        serializer= UserSerializer(user, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif req.method=="DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    





# get, put, post, delete