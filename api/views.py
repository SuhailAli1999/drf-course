from django.db.models import Max
from django.shortcuts import get_object_or_404
from api.serializers import ProductSerializer, OrderSerializer, ProductInfoSerializer
from api.models import Product, Order
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.views import APIView


class ProductsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

# class ProductsListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # lookup_url_kwarg = 'product_id'

class ProductsCreateAPIView(generics.CreateAPIView):
    model = Product
    serializer_class = ProductSerializer


# @api_view(['GET'])
# def products_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)

class ProductsDetailsAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# @api_view(['GET'])
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     serializer = ProductSerializer(product)
#     return Response(serializer.data)


class OrdersListListAPIView(generics.ListAPIView):
    queryset =  Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer

class UserOrdersListListAPIView(generics.ListAPIView):
    queryset =  Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        qs = super().get_queryset
        return qs.filter(user=self.request.user)


# @api_view(['GET'])
# def orders_list(request):
#     orders = Order.objects.prefetch_related('items__product')
#     serializer = OrderSerializer(orders, many=True)
#     return Response(serializer.data)

@api_view(['GET'])
def products_info(request):
    products = Product.objects.all()
    serializer = ProductInfoSerializer({
        'products' : products,
        'count' : len(products),
        'max_price' : products.aggregate(max_price=Max('price'))['max_price']
    })
    return Response(serializer.data)


class ProductInfoAPIView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductInfoSerializer({
            'products' : products,
            'count' : len(products),
            'max_price' : products.aggregate(max_price=Max('price'))['max_price']
        })
        return Response(serializer.data)