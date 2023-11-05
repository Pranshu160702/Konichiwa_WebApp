"""
URL configuration for Konichiwa project.

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
from Konichiwa import views
from konichiwa_app import views as appViews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homePage, name='homepage'),
    path("signup/", appViews.signupAction, name='signup'),
    path("signin/", appViews.signinAction, name='signin'),
]   
