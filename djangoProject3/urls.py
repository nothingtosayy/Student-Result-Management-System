"""djangoProject3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from clgresults.views import *
from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register, name='home'),
    path('result/', result, name='result'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('search/', search, name='search'),
    path('search/studentresult/', studentres, name='studentres'),
    path('contact/', contact, name='contact')
]
