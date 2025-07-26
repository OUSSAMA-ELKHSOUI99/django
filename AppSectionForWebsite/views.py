from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# we can have methods to send email, pull data from the database, transform data, etc.

def say_hello(request):
    """
    A simple view that returns a greeting.
    """
    return HttpResponse("Hello, welcome to our website!")