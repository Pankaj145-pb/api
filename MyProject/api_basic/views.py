from django.shortcuts import render
from django.http import HttpRequest,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import OrderSerializer
from .models import Product, Category, Order, User

# Create your views here.
@csrf_exempt
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return JsonResponse(serializer.data, safe=False)


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrderSerializer(data=data)

        if serializer.is_valid():
            serilizer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors,status=400)