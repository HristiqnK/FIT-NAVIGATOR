from django.shortcuts import render

def shop(request):
    return render(request, "onlineShop/onlineShop.html")

def exercise(request):
    return render(request, "onlineShop/exercise.html")
