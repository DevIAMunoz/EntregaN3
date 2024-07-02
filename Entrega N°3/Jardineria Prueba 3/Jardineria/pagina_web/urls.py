from django.urls import path
from django.contrib import admin
from django.urls import include, path
from . import views
from .views import forbidden_view

urlpatterns = [
    path ('', views.index, name='index'), 
    path ('Fertilizantes', views.Fertilizantes, name='Fertilizantes'),  
    path ('Herramientas', views.Herramientas, name='Herramientas'),
    path ('Maceteros', views.Maceteros, name='Maceteros'),
    path ('Semillas', views.Semillas, name='Semillas'),
    path ('crud', views.crud, name='crud'),
    path ('productosAdd', views.productosAdd, name='productosAdd'),
    path ('productos_del/<str:pk>', views.productos_del, name='productos_del'),
    path ('productos_findEdit/<str:pk>', views.productos_findEdit, name='productos_findEdit'),
    path ('productosUpdate', views.productosUpdate, name='productosUpdate'),
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('login', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_usuario, name='registro'),
    path('forbidden/', forbidden_view, name='forbidden'),
   
]
