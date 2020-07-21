# It has to made manually and should be named as urls.py only
# Copied and pasted from om/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="BlogHome"),
]
