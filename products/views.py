from django.http import HttpResponse
from django.shortcuts import render
from .models import Products

# Create your views here.

def prods(request):
    # Most Common products in the region
    return render(request,'products/prodhome.html')

def search(request):
    stext=request.GET['stext']
    products=Products.objects.all()
    prods=[]
    for product in products:
        if stext.upper() in product.product_name.upper() or stext in product.influencer.upper() or stext in product.product_seller.upper():
            prods.append(product)
    return render(request,'products/prodsearch.html',{'products':prods})