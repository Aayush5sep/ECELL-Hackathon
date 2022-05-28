from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.loginpage),
    path('sesignup/', views.sepage),
    path('bysignup/', views.bypage),
    path('loginse/', views.loginn),
    path('signupse/', views.signupse),
    path('signupby/', views.signupby),
    path('logout/',views.logot),
    path('me/', views.userinfo),
]