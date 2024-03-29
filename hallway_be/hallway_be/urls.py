"""hallway_be URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_user/', include('api_user.urls')),
    path('api_accessoAtti/', include('api_accessoAtti.urls')),
    path('api_peg/', include('api_peg.urls')),
    path('common/', include('common.urls')),
    path("accounts/", include("django.contrib.auth.urls")),  # to use django.auth and implement login page
]
