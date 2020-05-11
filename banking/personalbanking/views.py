from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from rest_framework.views import APIView

# from rest_framework import authentication, permissions
# from personalbanking.models import Customer

def index(request):
    return HttpResponse("reached pernal banking")

