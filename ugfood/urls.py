from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('list-all-food/', views.ListAllFood, name="list-all-food"),
    path('create-food/', views.CreateFood, name="create-food"),
    path('view-food/<int:pk>/', views.ViewFood, name="view-food"),
    path('update-food/<int:pk>/', views.UpdateFood, name="update-food"),
    path('delete-food/<int:pk>/', views.DeleteFood, name="delete-food"),
]