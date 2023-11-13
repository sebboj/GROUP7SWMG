from django.urls import path
from shoppingcart import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_to_cart/<int:bookID>/<str:username>/', views.addToCart, name='add book to cart'),
    path('del_from_cart/<int:bookID>/<str:username>/', views.delFromCart, name='delete book from cart'),
    path('show_cart/<str:username>/', views.getCartBooks, name='get books in cart'),
    path('cart_total/<str:username>/', views.getCartTotal, name='get cart total'),
]