from django.db import models
from django.utils.text import slugify

# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

    def __str__(self):
        return self.description
    

class Collection(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ["title"]
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default="-")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.CharField(max_length=255)
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotion = models.ManyToManyField(Promotion)
    def __str__(self):
        return self.title

class Customer(models.Model):
    MEMBERSHIP_CHOICE = [
        ("B", "Bronze"), ("S", "Silver"), ("G", "Gold")
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255, unique=True)
    birth_day = models.DateField(null=True)
    membership = models.CharField(max_length=255,
                                  choices=MEMBERSHIP_CHOICE, default="B")
    
    def __str__(self):
        return self.first_name
    
    
class Order(models.Model):
    STATUS_PENDING = 'P'
    STATUS_COMPLETE = 'C'
    STATUS_FAILED = 'F'
    PAYMANT_STATUS_CHOICE = [
        (STATUS_PENDING, "Pending"), (STATUS_COMPLETE, "Completed"), (STATUS_FAILED, "Failed")
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=2, choices=PAYMANT_STATUS_CHOICE, default=STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Adress(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
