from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 20)

class WorkoutExercise(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    sets = models.CharField(max_length = 100)
    weight = models.CharField(max_length = 100)
    reps = models.CharField(max_length = 100)
    typeofSet = models.CharField(max_length=100)
    Notes = models.TextField(blank=True)
    categories = models.ManyToManyField('Category', related_name='tags')
