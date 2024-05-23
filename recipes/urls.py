from django.urls import path
import recipes.views

urlpatterns = [
    path('', recipes.views.home),
    path('sobre/', recipes.views.sobre),
    path('contato/', recipes.views.contato),
]
