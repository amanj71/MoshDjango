from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_render, name="store_product_render"),
]
