from django.shortcuts import render

def bmr(request):
    if request.method == 'POST':
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        if not (weight and height and age and gender):
            return render(request, 'calculators/bmr.html', {'error': 'All fields are required'})

        weight = int(weight)
        height = int(height)
        age = int(age)

        if gender == 'male':
            result = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
        elif gender == 'female':
            result = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)
        else:
            result = None

        return render(request, 'calculators/bmr.html', {'result': round(result) if result else 'Invalid gender'})

    return render(request, "calculators/bmr.html")
