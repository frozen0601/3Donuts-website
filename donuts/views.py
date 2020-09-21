from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'donuts/index.html')

def head(request):
    return render(request, 'head/index.html')
