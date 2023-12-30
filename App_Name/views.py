from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Movies


# Create your views here.
def index(request):
    movies = Movies.objects.all()
    alaki = [('amanj', 20), ('Hafez', 19), ("Shohaib", 19), ("undertaker", 20)]
    return render(request, "index.html", {"movies" : movies})
    #mo = ", ".join([m.title for m in movies])
    #return HttpResponse(mo)

x = 12
y = 10



def detail(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    return render(request, "detail.html", {"movie": movie})
    #return HttpResponse(movie_id)
    