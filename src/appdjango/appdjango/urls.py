"""appdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from pages.views import home_view, about_view, contact_view#PASO 1 home_view
from products.views import product_detail_view, product_create_view, product_list_view, product_details_view#PASO 4 prod_det_view #PASO 6 prod_creat_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),#PASO 1
    path('about/', about_view, name='about'),#PASO 2
    path('contact/', contact_view, name='contact'),#PASO 2
    path('product/', product_detail_view),#PASO 4
    path('create/', product_create_view),#PASO 6
    path('product/list', product_list_view),#PASO 7
    path('product/<int:id>/', product_details_view),
]
