"""pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.admindocs import views
from django.urls import path, include


from pro import abcd,next

admin.site.site_header = "Rahul Website"
admin.site.site_title = "Rahul Admin Portal"
admin.site.index_title = "Welcome to Rahul website"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ok', abcd.xyz, name="abcd"),
    path('ab',next.run, name="next"),
    path('abc/', include('app1.urls')),
    path('', include('app2.urls')),
    path('B/', include("app3.urls"))
]
