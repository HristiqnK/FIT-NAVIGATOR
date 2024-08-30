from django.contrib import admin
from .models import Home_Workout
from .models import Busy_Workout
from .models import Free_Workout
from .models import Diet_Tips

admin.site.register(Home_Workout)
admin.site.register(Busy_Workout)
admin.site.register(Free_Workout)
admin.site.register(Diet_Tips)
