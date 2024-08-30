from django.db import models

class BaseWorkout(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    Exercise1 = models.TextField(max_length=100)
    Exercise2 = models.TextField(max_length=100)
    Exercise3 = models.TextField(max_length=100)
    Exercise4 = models.TextField(max_length=100)
    Exercise5 = models.TextField(max_length=100)
    Exercise6 = models.TextField(max_length=100)
    Exercise7 = models.TextField(max_length=100)
    Exercise8 = models.TextField(max_length=100)
    Exercise9 = models.TextField(max_length=100)
    Exercise10 = models.TextField(max_length=100)
    Exercise11 = models.TextField(max_length=100)
    Exercise12 = models.TextField(max_length=100)
    Exercise13 = models.TextField(max_length=100)
    Exercise14 = models.TextField(max_length=100)
    Exercise15 = models.TextField(max_length=100)
    Description = models.TextField(max_length=300, default='')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Home_Workout(BaseWorkout):
    pass

class Busy_Workout(BaseWorkout):
    pass

class Free_Workout(BaseWorkout):
    pass

class Diet_Tips(models.Model):
    name = models.CharField(max_length=50)
    goals = models.CharField(max_length=50)
    bodytype = models.CharField(max_length=50)
    Tip1 = models.TextField(max_length=400)
    Tip2 = models.TextField(max_length=400)
    Tip3 = models.TextField(max_length=400)
    Tip4 = models.TextField(max_length=400)
    Tip5 = models.TextField(max_length=400)

    def __str__(self):
        return self.name