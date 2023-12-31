from django.urls import path
from . import views


urlpatterns = [
    path('', views.submit_expense, name='submit_expense'),
    path('register', views.register, name='register'),
]