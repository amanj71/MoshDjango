from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('about/', views.about_page, name="about_page"),
    path('contact/', views.contact_page, name="contact_page"),
    path('login/', views.login_page, name="login_page"),
    path('register/', views.register_page, name="register_page"),
    path('products/', views.ProductListView.as_view(), name="products_list"),
    path('products/fbv<int:id>/', views.product_detail, name="product_detail"),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name="product-detail"),
    path('jquery', views.jquery, name="jquery"),
]