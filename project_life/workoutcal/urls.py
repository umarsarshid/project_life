from django.urls import path
from . import views


urlpatterns = [
    # path("", views.CalendarView.as_view(), name="workoutcaltoday"),
    path("", views.Calendar_index, name="calendar_index"),
    path("<str:month>", views.Calendar_Spec, name= "calendar_spec")
    ]
