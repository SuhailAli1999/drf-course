from django.urls import path
from . import views

urlpatterns = [
    # path('products/', views.products_list),
    path('products/', views.ProductsListAPIView.as_view()),
    path('products/info/', views.products_info),
    # path('product/<int:pk>/', views.product_detail),
    path('products/<int:pk>/', views.ProductsDetailsAPIView.as_view()),
    # path('orders', views.orders_list)
    path('products/<int:pk>/', views.OrdersListListAPIView.as_view()),

]
