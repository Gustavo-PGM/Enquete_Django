from django.urls import path
from . import views

urlpatterns = [
    path('', views.enquetes, name='enquetes'),
    path('votar/<int:pk>/', views.votos, name='votos'),
    path('resultados/<int:pk>/', views.resultados, name='resultados'),
]
