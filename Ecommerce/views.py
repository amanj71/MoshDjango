from typing import Any
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth import login, authenticate
from .forms import ContactPageForm, LoginForm, RegisterForm
from .models import Product

class ProductListView(ListView):
    queryset = Product.objects.all()
    model = Product
    template_name = "ecommerce/product_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        "product_detail": product
    }
    print(context)
    return render(request, "ecommerce/product_detail.html", context)
    pass

class ProductDetail(DetailView):
    model = Product
    template_name = "ecommerce/product_detail.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetail, self).get_context_data(*args, **kwargs)
        print("There is Prodect detail object")
        print(context)
        return context

# Create your functional views here.

def home_page(request):
    context = {
        "title": "This is Home Page",
        "content": "In this path you see HOME page",
        "logged_user": "User name"
    }
    if request.user.is_authenticated:
        context['logged_user'] = "Great, You are logged in. Enjoy more content :)"
    return render(request, "ecommerce/home_page.html", context)

def about_page(request):
    context = {
        "title": "This is ABOUT Page",
        "content": "In this path you see ABOUT page",
    }
    return render(request, "ecommerce/about_page.html", context)

def contact_page(request):
    contact_form = ContactPageForm(request.POST or None)
    context = {
        "title": "This is CONTACT Page",
        "content": "In this path you see CONTACT page",
        "form": contact_form,
    }
    print(request.POST.get("email"))
    if contact_form.is_valid():
        print (contact_form.cleaned_data)
    return render(request, "ecommerce/contact_page.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User Logged in:")
    print(request.user.is_authenticated)
    
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #context['form'] = LoginForm()
            return redirect("login_page")
        else:
            return HttpResponse("Error In Login Procesure")
    return render(request, "ecommerce/login_page.html", context)

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form, 
    }
    print("before Click Submit")
    if form.is_valid():
        print(form.cleaned_data)
        print("is validated passed")
    else:
        print("is validate NOT passed")
    return render(request, "ecommerce/register_page.html", context)



def jquery(request):
    context = {

    }
    return render(request, 'ecommerce/jquery_learning.html', context)