from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def anytime(request):
    return render(request, 'anytime.html')

def create(request):
    return render(request, 'anytime_create.html')