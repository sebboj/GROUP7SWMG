import pymongo
from pymongo import MongoClient
import json
from django.http import JsonResponse


# connect to database
client = pymongo.MongoClient("mongodb+srv://sss:123@cluster0.f0xb8zo.mongodb.net/")
db = client["bookstore"]
collection = db["books"]

#add book to shopping cart
def addToCart(request):
    try:
        book_id = request.get_json()
        user_id = request.get_json()
        data = {
            'isbn': book_id,
            'user_id': user_id,
        }
        return JsonResponse(data)
    except DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)

def delFromCart(request):
    try:
        user_id = ObjectId(user_id)
        book_to_delete = db.books.delete_one({"user_id": user_id, "book_id": book_id})
        if book_to_delete.deleted_count == 1:
            return JsonResponse(response=json.dumps({'message': 'Item deleted.'})

        return JsonResponse(response=json.dumps({'message': 'Nothing to delete.'})

    except Exception as ex:
        print(f"<{ex}>")
        return JsonResponse(response=json.dumps({'message': 'Error: cannot delete item.'})

def getCartBooks(request):
    try:
        book_id = request.get_json()
        user_id = request.get_json()
        data = {
            'isbn': book_id,
            'user_id': user_id,
        }

        query = {'user_id': user_key}
        books = list(db.books.find(query))

        if not books:
            return Response(response=json.dumps({'error': 'no books found for this user'}, default=str), status=404,
                            mimetype="application/json")

        for book in books:
            book.pop('_id')
            book.pop('user_id')

        return JsonResponse(data)

    except DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)

def getCartTotal(request):
    try:
        book_id = request.get_json()
        user_id = request.get_json()
        data = {
            'isbn': book_id,
            'user_id': user_id,
        }

        # search and find total
        query = {'user_id': user_id}
        books = list(db.books.find(query))
        tot = 0

        for book in books:
            if user_id == book.user_id:
                tot += book.price

        return JsonResponse(tot)
    except DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)