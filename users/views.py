from django.http import HttpResponse
from .models import userCollections
from rest_framework.decorators import api_view
from rest_framework.response import Response


#Simple Home screen
def home(request):
    return HttpResponse ('Welcome To Online Library')

#This method gets the information for a user provided that a username was specified in the url.
#if the username does not exist an error message will display
@api_view(['GET'])
def getData(request, username):
    user = userCollections.find_one({'username': username})

    if user:
        user_data = {
            "username": user.get("username", ""),
            "firstname": user.get("firstname", ""),
            "lastname": user.get("lastname", ""),
            "email_address": user.get("email_address", ""),
            "physical_address": user.get("physical_address", ""),
            "password": user.get("password", "")
        }
        return Response(user_data)
    else:
        return Response("Username is not in the database")


#This method adds a new user. Required fields must be filled out.
#It checks to see if fields were provided appropriately 
#it asks for a confirmation field for the password but that does not get inputed onto the database
#if username already exists it produces an error message  
@api_view(['GET', 'POST'])
def addUser(request):
    '''
        Required Fields: 
    
    {
        "username": "johndoe",
        "firstname": "John",
        "lastname": "Doe",
        "email_address": "johndoe@example.com",
        "physical_address": "123 Main St",
        "password": "password123",
        "confirm_password": "password123"
    }
    '''
    
    user_data = request.data

    username = user_data.get('username')
    fname = user_data.get('firstname')
    lname = user_data.get('lastname')
    eaddress = user_data.get('email_address')
    paddress = user_data.get('physical_address')
    password = user_data.get('password')
    cpassword = user_data.get('confirm_password')

    if not username or not fname or not lname or not eaddress or not paddress or not password or not cpassword:
        return Response({"Please provide all required fields"})

    if userCollections.find_one({'username': username}):
        return Response({"Username Already Exists! Registration Failed! Please Choose Another Username"})

    if password != cpassword:
        return Response({"Passwords did not match! Registration Failed"})

    records = {
        "username": username,
        "firstname": fname,
        "lastname": lname,
        "physical_address": paddress,
        "email_address": eaddress,
        "password": password,
    }
    userCollections.insert_one(records)
    return Response({"Your account has been successfully created!!"})
 
    
#This method updates the user information by asking the user to input a key:value pair to update the desired fields
#if a key does not exist in the database an error will be produced
#if username does not exist.. error is produced
#if user tries to change their username to a username that is already taken... error is produced
#if update is succesfull it will display a message else it will display an error message.
@api_view(['GET','PATCH'])
def update(request, username):
        '''
        Format Neeeded:
        
    {
        "Key": "Value"
    }
        
        
        Available Keys:
        username,
        firstname,
        lastname,
        physical_address,
        password
        
        if a credit card has been added you can update credit card by using key:
        credit_card
        
        
   
        '''
        user_data = request.data
        requested_user = userCollections.find_one({'username':username})
        
        for field in user_data:
            if field not in requested_user:
                return Response ("Key chosen is not an existing key in the database")
        
        if not requested_user:
            return Response('Username does not exist in the Database')
        
        new_username = request.data.get("username", "")
        existing_user = userCollections.find_one({'username': new_username})

        if existing_user:
            return Response({"Username already taken! Please choose another"})
        
        else:
            result = userCollections.update_one({"username": username}, {"$set": user_data})
            if result.modified_count > 0:
                return Response("update was successful!")
            else:
                return Response("Please follow the format provided")
            
#This method will add a credit card to the fields of a specific user provided a username in the search bar
#it updates the whole users information so a credit card can technically be updated here but it will just be replacing all the fields with new user information
#checks if user exist in the database 
#testing github  number two     
@api_view(['GET','POST'])
def add_card(request, username):
    credit_card_data = request.data.get('credit_card')

    if not credit_card_data:
        return Response("Add a Credit Card to your Profile!")

    existing_user = userCollections.find_one({'username': username})

    if not existing_user:
        return Response("User does not exist in the database")


    existing_user['credit_card'] = credit_card_data
    userCollections.replace_one({'username': username}, existing_user)

    return Response("Credit card added successfully!")


    
    