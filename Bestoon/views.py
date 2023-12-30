from django.shortcuts import render
from .models import User, Expense, Income
from django.http import JsonResponse
from json import JSONEncoder
from datetime import datetime

# Create your views here.
def submit_expense(request):
    this_token = request.POST['token']
    this_user = User.objects.filter()
    if date not in request.POST:
        date = datetime.now()
    
    Expense.objects.create(user=this_user, amount=request.POST['amount'], text=request.POST['text'], date=date)
    return JsonResponse({'status': 'OK'}, encoder=JSONEncoder)