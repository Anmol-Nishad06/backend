from django.http import HttpResponse
from django.shortcuts import render 

def home(request):
    """A simple view that returns a welcome message.
    return HttpResponse("Welcome to the backend core application!")"""
    return render(request, 'index.html')

def about(request):
    """A simple view that returns an about message."""
    return HttpResponse("This is the backend core application, providing essential functionalities.")

def contact(request):
    """A simple view that returns a contact message."""
    return HttpResponse("Contact us at: 626931***")  # Replace with actual contact info