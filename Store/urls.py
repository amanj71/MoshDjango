from django.urls import path
from . import views


urlpatterns = [
    path('', views.collection_render, name="store_collection_render"),
]
