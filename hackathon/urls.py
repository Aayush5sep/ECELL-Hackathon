"""                         Hackathon URL Configuration
analysis  ->  Analyze order prizes,selling quatity,selling areas,demand,inflation in prices etc.
dashboard  ->  User(Seller) Products Recommendation,Quantity Sold & Purchase,Money Management Dashboard
orders  -> User(Buyer) Orders Dashboard
sellerorders  ->  Products ordered by local retailers(Deep Discounting) in different areas
user  ->  User(Buyer & Seller) Basic Information(Name,Number,Email,Saved Payment Cards,Address etc.)
products  ->  Product Details added by different sellers
pagerank  ->  Sorting products to buyers based on location of buyer and sellers,prices,fast availability,
                easy delievery
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='Home Page'),
    # path('dashboard/',include('dashboard.urls')),
    # path('user/',include('user.urls')),
    # path('product/',include('products.urls')),
    # path('analyse/',include('analysis.urls')),
    # path('seller/',include('sellerorders.urls')),
    # path('priority/',include('pagerank.urls')),
    # path('orders/',include('orders.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
