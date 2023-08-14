"""
URL configuration for project23 project.

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
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mdb5/',mdb5,name='mdb5'),
    path('index/',index,name='index'),
    path('image/',image,name='image'),
    path('card/',card,name='card'),
    path('button/',button,name='button'),
    path('card1/',card1,name='card1'),
    path('button_group/',button_group,name='button_group'),
    path('dropdown/',dropdown,name='dropdown'),
    path('tooltips/',tooltips,name='tooltips'),
]
