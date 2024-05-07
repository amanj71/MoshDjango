from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.db.models import Value, F, Func, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Sum, Avg, Max, Min

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Collection, Product, Order, OrderItem, Customer
from .serializer import ProductSerializer

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



