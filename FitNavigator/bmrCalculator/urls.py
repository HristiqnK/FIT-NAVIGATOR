from django.urls import path, include
from . import views

urlpatterns = [
    path("bmr", views.bmr, name="bmr"),
]