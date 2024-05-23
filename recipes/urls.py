from django.urls import path
import recipes.views

urlpatterns = [
    path('', recipes.views.home),
    
]
