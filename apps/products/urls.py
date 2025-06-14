from django.urls import path
from . import views

urlpatterns = [
    path('hola/', views.hola_mundo, name='hola'),
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
]
