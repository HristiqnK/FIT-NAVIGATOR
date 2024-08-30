from django.urls import path, include
from . import views

urlpatterns = [
    path('fitNavigator', views.quiz, name="fitNavigator"),
    path('bmi', views.bmi, name="bmi"),
    path('results', views.results, name="results")
]