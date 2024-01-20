from django.shortcuts import render
from .forms import ContactPageForm, LoginForm

# Create your views here.
def home_page(request):
    context = {
        "title": "This is Home Page",
        "content": "In this path you see HOME page",
    }
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
    return render(request, "ecommerce/login_page.html", context)
