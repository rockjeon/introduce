from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def anytime(request):
    return render(request, 'anytime.html')