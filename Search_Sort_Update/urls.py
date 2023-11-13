from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('top10/', views.top_sold_books),    
    path('searchgenre/<str:genre>', views.searchgenre),
    path('rating/<str:rating>',views.books_by_rating),
    path('update/<str:publisher>/<str:discount>/', views.update_discount_by_publisher),

]
