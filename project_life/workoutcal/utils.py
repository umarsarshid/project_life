from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Category, WorkoutExercise


# HTMLCalender subobject that helps create the individual parts of the Calender. This will be called by the view function at time of page load so it can create the Calendar
class Calendar(HTMLCalendar):
    def __init__(self, year = None, month = None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
	# filter events by day
	def formatday(self, day, exerises):
		exerises_per_day = exerises.filter(start_time__day=day)
		d = ''
		for event in exerises_per_day:
			d += f'<li> {event.title} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr
    def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

    def formatmonth(self, withyear = True):
        exerises = WorkoutExercise.objects.filter(start_time__year=self.year, start_time__month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'

        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'

        cal += f'{self.formatweekheader()}\n'

        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, exerises)}\n'
		return cal
