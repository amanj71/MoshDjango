from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_render, name="store_product_render"),
    path('api/', views.product_list_api, name="product_list_api"),
]
