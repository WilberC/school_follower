"""school_follower URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from colegios.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', ListaTipos.as_view(), name='list_tipo'),
    url(r'^sub_tipos/$', ListaSubTipos.as_view(), name='list_sub_tipo'),
    url(r'^lista_colegios/$', ListaColegios.as_view(), name='list_cole'),
    url(r'^crear_colegios/$', CreateColegios.as_view(), name='create_cole'),
    url(r'^detalles_colegios/(?P<pk>\d+)$', DetallesColegios.as_view(), name='detalle_cole'),
    url(r'^create_actividad/(?P<pk>\d+)$', CreateActividad.as_view(), name='create_actividad'),

]
