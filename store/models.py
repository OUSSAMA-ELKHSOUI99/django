from django.db import models

# Create your models here.
# 
class Product(models.Model):
    sku = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Customer(models.Model):

    MEMBERSHIP_BASIC = 'B'
    MEMBERSHIP_PREMIUM = 'P'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BASIC, 'Basic'),
        (MEMBERSHIP_PREMIUM, 'Premium'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES , default=MEMBERSHIP_BASIC)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Order(models.Model):

    PAYMENT_STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('F', 'Failed')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='P')