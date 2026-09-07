from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view

# def home(request):
#     return HttpRequest("Home Page")

@api_view(["GET"])
def home(request):
    return Response("Hello")
