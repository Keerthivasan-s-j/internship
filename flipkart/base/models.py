from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User

class Product(models.Model):
    seller_name = models.CharField(verbose_name='Seller Name', max_length=50)
    seller_email = models.EmailField(verbose_name='Seller Email', max_length=50)
    # seller_phone = models.CharField(verbose_name='Seller Phone', max_length=10)
    # seller_address = models.TextField(verbose_name='Seller Address', max_length=10)
    prod_name = models.CharField(verbose_name='Product Name', max_length=50)
    prod_image = models.ImageField(verbose_name='Product Image', upload_to='images/')
    prod_details = models.TextField(verbose_name='Details', default='Product detail')
    prod_price = models.IntegerField(verbose_name='Product Price')
    prod_category = models.IntegerField(verbose_name='Category', choices=[
        (1, 'Electronics'),
        (2, 'Home'),
        (3, 'Fashon'),
    ])
    discount = models.IntegerField(verbose_name='Discount', default=0)

    def __str__(self) -> str:
        return self.prod_name.title()

class Feedback(models.Model):
    fname = models.CharField(verbose_name="First Name" ,max_length=50)
    lname = models.CharField(verbose_name="Last Name" ,max_length=50)
    email = models.EmailField(verbose_name="Email")
    ratings = models.IntegerField(choices=[
        (1,'Excelent'),
        (2,'Good'),
        (3,'Bad'),
    ])
    message = models.TextField(verbose_name="Message", max_length=1000)

    def __str__(self) -> str:
        return self.email

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username}"
    
class CartItem(models.Model):
    cart = models.ForeignKey(to=Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.prod_price * self.quantity

    def __str__(self):
        return self.product.prod_name
# Create your models here.
