from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import BookCollections
import pymongo
# Create your views here.
def home(request):
    return HttpResponse('hello world')

@api_view(['GET'])
def searchgenre(request, genre):
    books = BookCollections.find({'genre': genre})
    book_data = []
    for book in books:
        book_info = {
            "Genre": book.get("genre", ""),
            "PubYear": book.get("pubYear", ""),
            "Author": book.get("author", ""),
            "Publisher": book.get("publisher", ""),  
            "Description": book.get("desc", ""),
            "Price": book.get("priceUSD", ""),
            "Discount": book.get("discount", ""),
            "Rating": book.get("rating", ""),
            "Sold": book.get("numSold")
        }
        book_data.append(book_info)

    if book_data:
        return Response(book_data)
    else:
        return Response("Genre does not exist in the database")


@api_view(['GET'])
def top_sold_books(request):
    # Use the `find` method to query documents, sort by numSold in descending order, and limit to 10 results
    books = BookCollections.find().sort("numSold", -1).limit(10)

    book_data = []
    for book in books:
        book_info = {
            "Genre": book.get("genre", ""),
            "PubYear": book.get("pubYear", ""),
            "Author": book.get("author", ""),
            "Publisher": book.get("publisher", ""),  
            "Description": book.get("desc", ""),
            "Price": book.get("priceUSD", ""),
            "Discount": book.get("discount", ""),
            "Rating": book.get("rating", ""),
            "Sold": book.get("numSold")
        }
        book_data.append(book_info)

    if book_data:
        return Response(book_data)
    else:
        return Response("No books found in the database")


@api_view(['GET'])
def books_by_rating(request, rating):
    try:
        rating_value = float(rating)  # Convert the rating parameter to a float
    except ValueError:
        return Response("Invalid rating parameter. Please provide a valid number.")

    # Use the `find` method to query documents with a rating greater than or equal to the specified number
    books = BookCollections.find({'rating': {'$gte': rating_value}})

    book_data = []
    for book in books:
        book_info = {
            "Genre": book.get("genre", ""),
            "PubYear": book.get("pubYear", ""),
            "Author": book.get("author", ""),
            "Publisher": book.get("publisher", ""), 
            "Description": book.get("desc", ""),
            "Price": book.get("priceUSD", ""),
            "Discount": book.get("discount", ""),
            "Rating": book.get("rating", ""),
            "Sold": book.get("numSold")
        }
        book_data.append(book_info)

    if book_data:
        return Response(book_data)
    else:
        return Response(f"No books found with a rating greater than or equal to {rating}")


@api_view(['GET','PATCH'])
def update_discount_by_publisher(request, publisher, discount):
    try:
        discount_value = float(discount)  # Convert the discount parameter to a float
    except ValueError:
        return Response("Invalid discount parameter. Please provide a valid number.")

    # Use the `update_many` method to update documents with the specified publisher name
    result = BookCollections.update_many(
        {'publisher': publisher},
        {'$set': {'discount': discount}}
    )

    if result.modified_count > 0:
        return Response(f"Discount updated for books by {publisher}.")
    else:
        return Response(f"No books found with the publisher name {publisher}.")

  
