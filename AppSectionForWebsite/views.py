from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# we can have methods to send email, pull data from the database, transform data, etc.

def say_hello(request):
    # return HttpResponse("Hello, welcome to our website!")
    return render(request, 'hello.html', {"name": "oussama"})  # Render a template with a greeting message