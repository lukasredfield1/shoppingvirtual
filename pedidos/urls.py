from .import views
from django.urls import path


urlpatterns = [
    path('', views.procesar_pedidos, name="procesar_pedidos"),
    
]

