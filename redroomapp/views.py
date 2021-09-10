from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', context = {"products":products})
    
    






def payment(request):
    products = Product.objects.all()
    return render(request,'payment.html',context = {"products":products})

	

