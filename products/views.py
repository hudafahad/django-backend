from rest_framework import generics
from .models import Product
from .serializers import ProductSerializers
from .permissions import IsAdminOrReadOnly

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [IsAdminOrReadOnly]


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers    
    permission_classes = [IsAdminOrReadOnly]