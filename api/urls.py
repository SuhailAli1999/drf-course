from django.urls import path
from . import views

urlpatterns = [
    # path('products/', views.products_list),
    path('products/', views.ProductsListCreateAPIView.as_view()),
    # path('products/create', views.ProductsCreateAPIView.as_view()),

    path('products/info/', views.ProductInfoAPIView.as_view()),
    # path('product/<int:pk>/', views.product_detail),
    path('products/<int:pk>/', views.ProductsDetailsAPIView.as_view()),
    # path('orders', views.orders_list)
    path('orders/', views.OrdersListListAPIView.as_view()),
    path('user-orders/', views.UserOrdersListListAPIView.as_view()),

]
