from django.urls import path
from . import views

urlpatterns = [
    path('', views.city_view, name='city'),
    path('<int:city_id>/section/<int:section_id>/', views.section_view, name='section'),
    path('street/<int:street_id>/', views.street_view, name='street'),
]
