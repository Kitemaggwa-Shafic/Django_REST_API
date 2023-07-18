# Django REST API Project with Swagger

Django REST API Simple Project with Swagger

## Description
This a simple project showing and explaining in detail how a REST API is made and used in the Django framework and has been updated with Swagger, a combination of well-documented and interactive APIs. 
Swagger allows you to define, build, and document your APIs, whereas Django is a Python web framework that simplifies the process of building web applications.

This project explains how to build a Django REST API and Swagger from start to end.
It has models, views, and URLs, and all are well explained in detail.

## Requirements
1. Install djangorestframework for python using the command _**pip install djangorestframework**_
2. Install the swagger for Django, we shall use **drf-yasg** (Yet Another Swagger Generator) library. This library is a simple way to generate Swagger/OpenAPI specifications for your Django REST Framework (DRF) APIs.
   -> To install use the command  _**pip install drf-yasg**_
   
4. Make necessary configurations and changes to the setting.py file to cater for the new requirements in (1) and (2),
   -> Also configure the Swagger setting in the same file too.
   Setting.py file
   **Installed_Apps=
         [
         'rest_framework',
          'drf_yasg',
         ]**
6. Create an api_info.py file and add url path to use
7. run your server finally
    
## Screen Shot with Swagger API
![image](https://github.com/Kitemaggwa-Shafic/Django_REST_API/assets/54108967/6c0318c9-bafc-42b1-84a2-1afff846ec51)
