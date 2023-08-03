from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisements(request):
    return render(request, 'advertisement.html')

# Create your views here.
