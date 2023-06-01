"""
URL configuration for core project.

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
from brotherInCode import views
from brotherInCode.views import *

base = 'api/'

urlpatterns = [
    path(base+'admin/', admin.site.urls),
    path('', views.lista_tutores, name='lista_tutores'),
    path('tutores/', views.lista_tutores, name='lista_tutores'),
    path('quem-somos/', views.quem_somos, name='quem-somos'),
    path('tutor/<int:id_tutor>/', views.perfil_tutor, name='detalhe_tutor'),
    path('tutorias/', tutorias, name='tutorias'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
]
