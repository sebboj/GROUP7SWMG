from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('get/<str:username>/', views.getData),
    path('add/', views.addUser),
    path('update/<str:username>/', views.update),
    path('add_card/<str:username>/', views.add_card)
]
