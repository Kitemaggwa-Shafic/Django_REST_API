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
def ListAllFood(request):
    allFood = Food.objects.all()
    # setting serializer variable to FoodSerializer class pass in allfood variable and 
    # (many => True)return all fields
    serializer = FoodSerializer(allFood, many = True)
    # return a serialized representation of the food item as the response body. This serialized 
    # representation is obtained from the (serializer.data) attribute, which returns a dictionary of the serialized data.
    return Response(serializer.data)


# RESTAPI Function to return a certain food basing on id
@api_view(['GET'])
def ViewFood(request, pk):
    selectedFood = Food.objects.get(id=pk)
    serializer = FoodSerializer(selectedFood)
    return Response(serializer.data)


#  RESTAPI Function for creating new food
@api_view(['POST'])
def CreateFood(request):
    # serializer variable gets data from FoodSerializer class and the pass data from the UI
    serializer = FoodSerializer(data=request.data)
    # Checking if the data sent is valid be4 saving the data
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# RESTAPI Function for Updating new food
@api_view(['POST'])
def UpdateFood(request, pk):
    # This method retrieves a single instance of the Food model with the given primary key pk.
    food = Food.objects.get(id=pk)
    # Argument set to the retrieved food instance, and the data argument set to the request data. 
    # This initializes a serializer instance that can be used to serialize and deserialize instances of the Food model.
    serializer = FoodSerializer(instance=food, data=request.data)
    # This checks if the incoming data is valid for the Food model based on the serializer's defined validation rules. 
    # If the data (is_valid), the serializer.validated_data attribute is populated with the validated data.
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# Delete function
@api_view(['GET'])
def DeleteFood(request, pk):
    deletefood = Food.objects.get(id=pk)
    deletefood.delete()
    return Response("Food deleted successfuly !!")
