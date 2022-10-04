from django.contrib import admin
from workoutcal.models import Category, WorkoutExercise
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass

class WorkoutExerciseAdmin(admin.ModelAdmin):
    pass

admin.site.register(WorkoutExercise,WorkoutExerciseAdmin)
admin.site.register(Category,CategoryAdmin)
