from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.db.models import Value, F, Func, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Sum, Avg, Max, Min

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Collection, Product, Order, OrderItem, Customer
from .serializer import ProductSerializer, CollectionSerializer

# Create your views here.
def promotion_render(request):
    pass

def collection_render(request):
    pass

def product_render(request):
    #queryset = Product.objects.select_related('collection').all()
    #discount_calc = ExpressionWrapper(F('price')*0.8, output_field=DecimalField())
    #annotate_value = Order.objects.annotate(discount_field=discount_calc)
    queryset = Order.objects.all()[len(Order.objects.all())-5:]
    products_count = queryset.count()
    mathmatical_operation = OrderItem.objects.filter(product=1).aggregate(num_pro1_sold=Count('id'))
    context = {
        'products': queryset,
        'products_count': products_count,
        'calculation': mathmatical_operation,
        #'annotation': annotate_value
    }
   
    return render(request, 'store/products_list.html', context)

def customer_render(request):
    pass

def order_render(request):
    pass 

def orderitem_render(request):
    pass

def adress_render(request):
    pass

def cart_render(request):
    pass

def cartitem_render(request):
    pass

# Create Your API Views Here
@api_view(['GET', 'POST'])
def product_list_api(request):
    if request.method == 'GET':
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data
            return Response('Data is Validate')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def product_detail_api(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def collection_list_api(request):
    if request.method == "GET":
        queryset = Collection.objects.all()
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def collection_detail_api(request, id):
    collection = get_object_or_404(Collection, id=id)
    if request.method == "GET":
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CollectionSerializer(collection, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
