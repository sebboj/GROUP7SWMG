from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_to_cart/<str:ISBN>/<str:uid>/', views.addToCart, name='add book to cart'),
    path('del_from_cart/<str:ISBN>/<str:uid>/', views.delFromCart, name='delete book from cart'),
    path('show_cart/<str:uid>/', views.getCartBooks, name='get books in cart'),
    path('cart_total/<str:uid>/', views.getCartTotal, name='get cart total'),
]