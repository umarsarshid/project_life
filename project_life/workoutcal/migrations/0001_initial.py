# Generated by Django 4.1.1 on 2022-10-04 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('sets', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('reps', models.CharField(max_length=100)),
                ('typeofSet', models.CharField(max_length=100)),
                ('Notes', models.TextField(blank=True)),
                ('categories', models.ManyToManyField(related_name='tags', to='workoutcal.category')),
            ],
        ),
    ]