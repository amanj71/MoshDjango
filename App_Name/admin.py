from django.contrib import admin
from .models import Genre, Movies

class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'realese_year', 'genre')
# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movies, MovieAdmin)

