from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('increment/<int:cart_id>/', views.increment_cart, name='increment_cart'),
    path('decrement/<int:cart_id>/', views.decrement_cart, name='decrement_cart'),
    path('remove/<int:cart_id>/', views.remove_cart, name='remove_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders_page, name='orders'),
    path('place-order/', views.place_order, name='place_order'),
]