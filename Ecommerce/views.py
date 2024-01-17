from django.shortcuts import render

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
    context = {
        "title": "This is CONTACT Page",
        "content": "In this path you see CONTACT page",
    }
    return render(request, "ecommerce/contact_page.html", context)