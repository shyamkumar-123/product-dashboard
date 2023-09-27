"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from blogapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home),
    path('about',views.about),
    path('static',views.staticfile),
    path('addproduct',views.addproduct),
    path('dashboard',views.dashboard,name="dashboard"),
    path('delete/<rid>',views.delete,name="delete"),
    path('Edit/<rid>',views.edit,name="edit"),
    path('catfilter/<cv>',views.catfilter,name="catfilter"),
    path('statusfilter/<sv>',views.statusfilter,name="statusfilter"),
    path('sort/<x>',views.sortfilter,name='sortfilter'),
    path('filprice/<x>',views.pricefilter,name="pricefilter"),
    path('multifilter',views.multifilter),
    path('djforms',views.django_form,name="djforms"),
    path('modelform',views.modelform),
    path('success',views.user_register),
    path('login',views.user_login),
    path('setcookie',views.setcookie),
    path('getcookie',views.getcookie),
    path('session',views.setsession),
    path('getsession',views.getsession),
]
