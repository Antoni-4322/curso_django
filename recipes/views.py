from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, get_list_or_404
from .models import Recipe
from django.http import HttpResponse
# Create your views here.


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')


    return render(request, 'recipes/pages/home.html', context={'recipes': recipes})



def category(request, category_id):
    # recipes = Recipe.objects.filter(
    #     category__id=category_id, is_published=True
    # ).order_by('-id')

    # if not recipes:
    #     raise(Http404('Not Found '))

    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id, 
            is_published=True
        ).order_by('-id')
    )

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category |'
    })

def recipes(request, id):
     recipe = Recipe.objects.filter(pk=id, is_published=True).order_by('-id').first()

     return render(request, 'recipes/pages/recipe-view.html', context={'recipe': recipe, 'is_detail_page': True})

