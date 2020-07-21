"""om URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#  Don't forget to add blog and app in the settings.py file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),  # Tells that when 'shop/' is entered, then the code
    #  will be redirected towards the urls.py inside the shop app which will have it's own links
    path('blog/', include('blog.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
