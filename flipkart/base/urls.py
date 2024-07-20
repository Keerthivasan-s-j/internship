from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('feedback/', views.add_feedback, name='feedback'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('buy', views.buy, name='buy'),
    path('buy-from-cart', views.buy_from_cart, name='buy_from_cart'),
    path('addproduct/', views.add_product, name='addproduct'),
]