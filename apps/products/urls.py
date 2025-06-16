from django.urls import path
from . import views

urlpatterns = [
    # Ruta para listar y crear productos
    path('products/', views.product_list, name='product-list'),
    
    # Ruta para operaciones sobre un producto individual (obtener, actualizar, eliminar)
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
]
