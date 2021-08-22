from django.contrib.auth.models import User,auth
from django.contrib import messages 
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect,get_object_or_404
from shop.models import *
from . models import *


# Create your views here.


def cart_details(request,tot=0,count=0,cart_items=None):
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
        cart_items=items.objects.filter(cart=ct,active=True)
        for i in cart_items:
            tot +=(i.prodt.price*i.quan)
            count+=i.quan
    except ObjectDoesNotExist:
        pass        
    return render(request,'cart.html',{'ci':cart_items,'t':tot,'cn':count})

def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id    



def add_cart(request,product_id):
    prod=products.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items=items.objects.get(prodt=prod,cart=ct)
        if c_items.quan < c_items.prodt.stock:
            c_items.quan+=1
        c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(prodt=prod,quan=1,cart=ct)
        c_items.save()        
    return redirect('cartDetails')

def min_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(prodt=prod,cart=ct)
    if c_items.quan>1:
        c_items.quan-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartDetails')        

def cart_delete(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(prodt=prod,cart=ct)
    c_items.delete()
    return redirect('cartDetails')


#####
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('cart/register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already used')
                return redirect('cart/register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('cart/login')
        else:
            messages.info(request,'Password not same')
            return redirect('cart/register')
    else:
        return render(request,'register.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'User is invalid')
            return redirect('login')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')