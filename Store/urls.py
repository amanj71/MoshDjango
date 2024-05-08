from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_render, name="store_product_render"),
    path('api/', views.product_list_api, name="product_list_api"),
    path('api/<int:id>/', views.product_detail_api, name="product_detail_api"),
    path('api/collection/', views.collection_list_api, name="collection_list_api"),
    path('api/collection/<int:id>', views.collection_detail_api, name="collection_detail_api"),
]
