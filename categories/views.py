from django.shortcuts import render

from .models import Category

def home(request):
    categories = Category.objects
    return render(request, 'categories/home.html', {'categories':categories})
