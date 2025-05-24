from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products_list),
    path('products/info/', views.products_info),
    path('product/<int:pk>/', views.product_detail),
    path('orders', views.orders_list)

]
