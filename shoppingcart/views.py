from django.http import HttpResponse
from .models import users, cart, inv
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def home(request):
    return HttpResponse('Selam World')


#add book to shopping cart
@api_view(['POST'])
def addToCart(request, bookID, username):
    if not users.find_one({'username': username}):
        return Response({'ERROR: User does not exist'})

    if not inv.find_one({'ISBN': bookID}):
        return Response({'ERROR: Book does not exist'})

    entry = {
        'ISBN': bookID,
        'username': username,
    }
    cart.insert_one(entry)

    return Response({'Book has been successfully added to user cart'})


#delete book from shopping cart
@api_view(['DELETE'])
def delFromCart(request, bookID, username):
    entry = cart.find_one({'ISBN': bookID, 'username': username})
    if not entry:
        return Response({'ERROR: Cart entry for given user and book does not exist'})

    cart.delete_one(entry)
    return Response({'Cart entry has been successfully deleted'})


#get list of books from a user's cart
@api_view(['GET'])
def getCartBooks(request, username):
    book_list = []
    user_cart = cart.find({'username': username})

    for book in user_cart:
        currISBN = book.get('ISBN', '')
        book_info = inv.find_one({'ISBN': currISBN})
        curr = {
            'ISBN': book_info.get('ISBN', ''),
            'name': book_info.get('name', ''),
            'desc': book_info.get('desc', ''),
            'priceUSD': book_info.get('priceUSD', ''),
            'author': book_info.get('author', ''),
            'genre': book_info.get('genre', ''),
            'publisher': book_info.get('publisher', ''),
            'pubYear': book_info.get('pubYear', ''),
            'numSold': book_info.get('numSold', ''),
            'discount': book_info.get('discount', ''),
            'rating': book_info.get('rating', ''),
        }
        book_list.append(curr)

    if book_list:
        return Response(book_list)
    else:
        return Response({'User has no books in their cart'})


#get the usd total from a user's cart
@api_view(['GET'])
def getCartTotal(request, username):
    subtotal = 0
    books = cart.find({'username':username})

    for book in books:
        subtotal += inv.find_one({'ISBN': book.get('ISBN', '')}).get('priceUSD', '')

    if books:
        return Response(subtotal)
    else:
        return Response({"User has no books in their cart"})


