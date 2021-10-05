from django.urls import path

from .api_views import (
    CategoryListAPIView, 
    CustomersListAPIView,
    OrdersListAPIView,
    CategoryAPIView,
    ProductAPIView,
    ProductListAPIView,
    OrdersAPIView
)
urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories_lsit'),
    path('categories/<str:id>', CategoryAPIView.as_view(), name='categories_detail'),
    path('customers/', CustomersListAPIView.as_view(), name='customers_list'),
    path('orders/', OrdersListAPIView.as_view(), name='orders_list'),
    path('orders/<str:id>', OrdersAPIView.as_view(), name='orders_detail'),
    path('products/', ProductListAPIView.as_view(), name='products_list'),
    path('products/<str:id>', ProductAPIView.as_view(), name='products_detail'),
]