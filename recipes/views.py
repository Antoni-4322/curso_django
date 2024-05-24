from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html', context={'name': 'Antonio Sousa'})


def recipes(request, id):
   
    return render(request, 'recipes/pages/recipe-view.html', context={'name': 'Antonio Sousa'})

