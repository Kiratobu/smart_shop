from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from .serializers import CategorySerializer, CustomerSerializer, OrderSerializer, BaseProductSerializer
from rest_framework.filters import SearchFilter
from ..models import Category, Customer, Order, Product


class Pagination(PageNumberPagination):

    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10

class CategoryListAPIView(ListAPIView):

    serializer_class = CategorySerializer
    pagination_class = Pagination
    queryset = Category.objects.all()

class CategoryAPIView(RetrieveUpdateAPIView, ListCreateAPIView, RetrieveDestroyAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'

class ProductListAPIView(ListAPIView):
    serializer_class = BaseProductSerializer
    pagination_class = Pagination
    queryset = Product.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']

class ProductAPIView(RetrieveUpdateAPIView, ListCreateAPIView, RetrieveDestroyAPIView):

    serializer_class = BaseProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'

class CustomersListAPIView(ListAPIView):
    serializer_class = CustomerSerializer
    pagination_class = Pagination
    queryset = Customer.objects.all()

class OrdersListAPIView(ListAPIView):
    serializer_class = OrderSerializer
    pagination_class = Pagination
    queryset = Order.objects.all()

class OrdersAPIView(RetrieveUpdateAPIView, ListCreateAPIView, RetrieveDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = 'id'