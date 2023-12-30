"""
URL configuration for MoshDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 

# admin panel labels
admin.site.site_header = "Amanj Learning Django"
admin.site.index_title = "Admin Panel"

# add main urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path("appadress/", include("App_Name.urls")),
    path("djangocourse/", include("DjangoCourse.urls")),
    path("store/", include("Store.urls")),
    path("testapp/", include("TestApp.urls")),
    path("bestoon/", include("Bestoon.urls")),
]
