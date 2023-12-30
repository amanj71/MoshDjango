from django.contrib import admin
from . import models

# create your AdminModel class here
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("title",)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'collection')

class PromotionAdmin (admin.ModelAdmin):
    list_display = ("description","discount",)

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "membership",)
    list_editable = ("membership",)
    list_per_page = 10

# Register your models here.
admin.site.register(models.Collection, CollectionAdmin) 
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Promotion, PromotionAdmin)