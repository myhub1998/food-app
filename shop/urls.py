from typing_extensions import ParamSpec
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>',views.prodDetails,name='details'),
    path('search',views.searchDetails,name='search'),
    path('logout',views.logout,name='shop/logout'),
]
