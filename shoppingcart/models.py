from django.db import models
from .db_connection import db

# Create your models here.
users = db['users']
cart = db['cart']
inv = db['books']