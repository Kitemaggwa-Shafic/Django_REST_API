from django.shortcuts import render

'''
import the Response object and @apiview decorator from the Django REST framework.
Response helps return sterilized data in JSON format while the @apiview displays the API.
'''
from rest_framework.response import Response
from rest_framework.decorators import api_view



from .models import Food
from .serializer import FoodSerializer


# Create your views here.


@api_view(['GET'])
def getFood(request):
    food = Food.objects.all()
    serializer = FoodSerializer(food, many = True)
    return Response(serializer.data)


@api_view(['POST'])
def postFood(request):
    serializer = FoodSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
