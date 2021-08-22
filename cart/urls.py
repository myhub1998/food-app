from django.urls import path
from . import views

urlpatterns=[
    path('cartDetails',views.cart_details,name='cartDetails'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('cart_decrease/<int:product_id>/',views.min_cart,name='cart_decrement'),
    path('remove/<int:product_id>/',views.cart_delete,name='cartdelete'),
    path('register',views.register,name='cart/register'),
    path('login',views.login,name='cart/login'),
    path('logout',views.logout,name='cart/logout'),
]