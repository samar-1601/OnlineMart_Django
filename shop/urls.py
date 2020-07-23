# It has to made manually and should be named as urls.py only

from django.contrib import admin    # Copied and pasted from om/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="About"),
    path('contact/', views.contact, name="Contact"),
    path('tracker/', views.tracker, name="Tracker"),
    path('search/', views.search, name="Search"),
    path('productview/<int:myid>', views.productView, name="ProductView"),
    path('checkout/', views.checkout, name="Checkout"),
]
