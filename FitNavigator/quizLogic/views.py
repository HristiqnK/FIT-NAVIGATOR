import json
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from .models import Home_Workout, Busy_Workout, Free_Workout, Diet_Tips
import random

def quiz(request):
    if request.method == "POST":
        env = request.POST.get('env')
        gender = request.POST.get('gender')
        goals = request.POST.get('goals')
        time = request.POST.get('time')
        bodytype = request.POST.get('bodytype')

        all_workouts = []
        diet_tips = []

        if env == "home":
            all_workouts = list(Home_Workout.objects.filter(gender=gender))
        elif env == "gym":
            if time == "busy":
                all_workouts = list(Busy_Workout.objects.filter(gender=gender))
            else:
                all_workouts = list(Free_Workout.objects.filter(gender=gender))

        random.shuffle(all_workouts)

        all_workouts_serializable = [model_to_dict(workout) for workout in all_workouts]
        diet_tips = list(Diet_Tips.objects.filter(goals=goals, bodytype=bodytype))

        diet_tips_serializable = [model_to_dict(tip) for tip in diet_tips]

        request.session['all_workouts'] = all_workouts_serializable
        request.session['diet_tips'] = diet_tips_serializable
        request.session['current_index'] = 0

        return redirect('results')

    return render(request, "Quiz/quiz.html")

def results(request):
    all_workouts = request.session.get('all_workouts', [])
    diet_tips = request.session.get('diet_tips', [])
    current_index = int(request.session.get('current_index', 0))

    if request.method == 'POST' and 'next_button' in request.POST:
        current_index += 1

    request.session['current_index'] = current_index

    if current_index < len(all_workouts):
        current_workout = all_workouts[current_index]
    else:
        current_workout = None

    if request.method == 'POST' and 'save_workout' in request.POST:
        return

    return render(request, "Quiz/results.html", {'current_workout': current_workout, 'diet_tips': diet_tips})

def bmi(request):
    if request.method == 'POST':
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        
        if weight and height:
            try:
                weight = float(weight)
                height = float(height)
                result = weight / (height / 100) ** 2
                return render(request, 'calculators/bmi.html', {'result': round(result, 2)})
            except ValueError:
                return render(request, 'calculators/bmi.html', {'error': 'Invalid input. Please enter numeric values for weight and height.'})
        else:
            return render(request, 'calculators/bmi.html', {'error': 'Please provide both weight and height.'})
    
    return render(request, "calculators/bmi.html")