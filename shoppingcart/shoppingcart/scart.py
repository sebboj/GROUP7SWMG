import pymongo
from pymongo import MongoClient
import json
from django.http import JsonResponse


# connect to database
try:
    mongo = MongoClient('mongodb+srv://sss:123@cluster0.f0xb8zo.mongodb.net/')
    mongo.server_info()
    db = mongo.cart
except:
    print('ERROR - unable to connect to database')

#add book to shopping cart
def add2cart(request):
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