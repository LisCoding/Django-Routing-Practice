from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def login(request):
    response = "placeholder for users to login"
    return HttpResponse(response)

def register(request):
    response = "placeholder for users to create a new user record"
    return HttpResponse(response)

def show(request):
    response =  "placeholder to later display all the list of users"
    return HttpResponse(response)
