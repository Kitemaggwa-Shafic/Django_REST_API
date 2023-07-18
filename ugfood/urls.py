from django.urls import path
from . import views
from django.conf import settings
# 
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from .api_info import api_info


schema_view = get_schema_view(
    info=api_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('list-all-food/', views.ListAllFood, name="list-all-food"),
    path('create-food/', views.CreateFood, name="create-food"),
    path('view-food/<int:pk>/', views.ViewFood, name="view-food"),
    path('update-food/<int:pk>/', views.UpdateFood, name="update-food"),
    path('delete-food/<int:pk>/', views.DeleteFood, name="delete-food"),
    # Modifying with swagger
    path('', views.index, name="index"),
]

# 
# Include the Swagger and ReDoc URLs
urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
