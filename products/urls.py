from django.urls import path
from . import views
urlpatterns = [
    path('', views.prods),
    path('search/', views.search),
]