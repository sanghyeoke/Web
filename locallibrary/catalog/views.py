from django.shortcuts import render

# Create your views here.

def hello(reqeust):
    print(reqeust)
    return print("HI")