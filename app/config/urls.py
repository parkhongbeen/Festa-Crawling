"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

<<<<<<< HEAD
urlpatterns_api =[
    path('members/', include('members.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urlpatterns_api)),
    path('accounts/', include('allauth.urls')),
=======
from members.views import signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
    path('', signup_view, name='signup'),
>>>>>>> fec807a7ff750d31da9e3811fa9297160feca680
]
