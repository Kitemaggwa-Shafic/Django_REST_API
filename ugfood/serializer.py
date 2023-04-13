
'''
Serializers convert complex Django models to JSON objects, making data easyto read on the API. 
Serializing makes data more readable on the API.
'''

# import serializers module from the rest_framework package 
from rest_framework import serializers
from .models import Food

# create a FoodSerializer class that inherits from the ModelSerializer class.
'''
FoodSerializer which extends the (serializers.ModelSerializer) provided by the Django REST Framework. 
This means that the FoodSerializer class inherits all of the functionality of the base serializer 
class and can also define additional serialization behavior specific to the Food model.
'''

# class FoodSerializer is used to convert complex Food model instances to and from JSON format, 
# which can be easily consumed by web APIs.
class FoodSerializer(serializers.ModelSerializer):

    # Meta class within the FoodSerializer class  is used to provide metadata about the FoodSerializer class, 
    # such as which model to serialize and which fields to include in the serialized representation.
    class Meta:
        # the Food model you want to serialize and the fields you want to add to the API
        # Food model that the serializer should use to create the serialized representation. 
        # This means that the serializer will convert instances of the Food model to and from JSON format.
        model = Food
        # Below specifies which fields from the Food model should be included in the serialized representation. 
        # In this case, the name and description
        fields = ('name', 'description')
