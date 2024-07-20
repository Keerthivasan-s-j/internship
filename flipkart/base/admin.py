from django.contrib import admin
from .models import Product,Feedback,Cart,CartItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ['seller_name', 'seller_email', 'prod_name', 'prod_image', 'prod_details', 'prod_price', 'prod_category', 'discount']

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'email', 'ratings', 'message']


admin.site.register(Product, ProductAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)
# Register your models here.
