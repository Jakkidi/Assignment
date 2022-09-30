from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import product,cart
from .serializer import productSerializer
# Create your views here.
@api_view(['GET','post','put'])
def quick_start(request):
    if request.method=='GET':
        data=product.objects.all()
        res=productSerializer(data)
        return Response(res)
    elif request.method=='POST':
        res=productSerializer(data=data)
        return Response (res)
@api_view(['GET'])
def getdetails(request,title):
    res=product.objects.get(title=title)
    return Response(res) 
    