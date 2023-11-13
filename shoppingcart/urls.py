from django.urls import path
from shoppingcart import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_to_cart/<int:bookID>/<int:userID>/', views.addToCart, name='add book to cart'),
    path('del_from_cart/<int:bookID>/<int:userID>/', views.delFromCart, name='delete book from cart'),
    path('show_cart/<int:userID>/', views.getCartBooks, name='get books in cart'),
    path('cart_total/<int:userID>/', views.getCartTotal, name='get cart total'),
]