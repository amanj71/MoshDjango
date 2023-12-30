import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from Store.models import Customer


# Create your views here.
def say_hello(request):
    start_date = datetime.date(1990, 1, 1)
    end_date = datetime.date(2005, 3, 31)
    #customers = Customer.objects.filter(membership="G")
    #customers = Customer.objects.filter(birth_day__range=(start_date, end_date))
    #customers = Customer.objects.filter(email__contains=".org")
    customers = Customer.objects.values("first_name", "membership").order_by("birth_day")
    context = {"data_render": customers}
    return render(request, "djangocourse/djangocourse.html", context)
    #return HttpResponse("this is done by httpresponse")