"""VITW URL Configuration

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
from django.urls import path,include
from secondapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sowbhanu/',views.sample),
    path('center/',views.centerexample),
    path('task/',views.taskfun),
    path('integervalue/<int:num>/',views.integervalueex),
    path('Stringvale/<str:name>/',views.stringvalueex),
    path('exa/<int:num>/<str:name>/',views.example),
    path('samplehtml/',views.samplehtmlex,name='samplehtmlex'),
    path('demo/',views.htmlexcss,name=''),
    path('s/',views.htmlex),
    path('boostrapex/',views.boostrapex,name=''),
    path('vijayaclg/',views.vijayaclg,name=''),
    path('VITWCollege/',views.VITWCollege,name=''),
    path('details/',views.details,name='details'),
    path('',include('thirdapp.urls')),
    path('forms/',include('formsapp.urls')),
]
    