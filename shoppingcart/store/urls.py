from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_to_cart', views.addToCart, name='add book to cart'),
    path('del_from_cart', views.delFromCart, name='delete book from cart'),
    path('show_cart', views.getCartBooks, name='get books in cart'),
    path('cart_total', views.getCartTotal, name='get cart total')
]