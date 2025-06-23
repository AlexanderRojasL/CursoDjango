from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


# ------------------------------
# VISTA PARA LISTAR Y CREAR PRODUCTOS
# ------------------------------
@api_view(['GET', 'POST'])
def product_list(request):
    """
    GET: Devuelve una lista de todos los productos.
    POST: Crea un nuevo producto con los datos enviados en el cuerpo de la solicitud.
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data) #responde con la lista en formato JSON

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() #guarda el nuevo producto en la base de datos
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        #Si los datos no son validos devuelve errores
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

# ------------------------------
# VISTA PARA DETALLE, ACTUALIZACIÓN Y ELIMINACIÓN DE UN PRODUCTO
# ------------------------------
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    """
    GET: Devuelve los datos de un producto por su ID (pk).
    PUT: Actualiza los datos de un producto.
    DELETE: Elimina el producto.
    """
    try:
        #obtiene el producto por su id (primary key)
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)