"""
URL configuration for DataWareHouse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from main import views
from CRM.views import MoneyView
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('register', views.register , name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('taskmanager', views.MyTasks.as_view(), name='taskmanager'),
    path('delete-data/', views.MyTasks.delete_data, name='delete_data'),
    path('money', MoneyView.as_view(), name= 'money'),
    path('calc',MoneyView.calc , name = 'calc' ),
    path('delete-zadacha', MoneyView.delete , name = 'delete'),
    path('delete-selected', views.MyTasks.delete_selected, name='delete_selected'),
    path('change-password', views.change_password, name='change_password'),
    path('price', views.price, name='price'),
    path('price-sus' , views.purchase, name='price-sus')
]
