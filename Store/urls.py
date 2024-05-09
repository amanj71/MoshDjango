from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_render, name="store_product_render"),

    ## API VIEWS
    # functinal api
    path('api/', views.product_list_api, name="product_list_api"),
    path('api/<int:id>/', views.product_detail_api, name="product_detail_api"),
    path('api/collection/', views.collection_list_api, name="collection_list_api"),
    path('api/collection/<int:id>', views.collection_detail_api, name="collection_detail_api"),
    # class based api
    path('apiclass/', views.ProductListAPI.as_view(), name="ProductListAPI"),
    path('apiclass/<int:pk>/', views.ProductDetailAPI.as_view(), name="ProductDetailAPI"),
    path('apiclass/collection/', views.CollectionListAPI.as_view(), name="CollectionListAPI"),
    path('apiclass/collection/<int:pk>/', views.CollectionDetailAPI.as_view(), name="CollectionDetailAPI"),
]
