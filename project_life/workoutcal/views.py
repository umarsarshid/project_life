from datetime import datetime
from datetime import date
from datetime import timedelta
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import date

from .models import *
from .utils import Calendar

# Create your views here.
def Calendar_index(request):
    today = date.today()
    cal = Calendar(today.year, today.month)
    # Call the formatmonth method, which returns our calendar as a table
    html_cal = cal.formatmonth(withyear=True)
    calendar = mark_safe(html_cal)
    prevmonth =prev_month(today)
    nextmonth = next_month(today)
    context = {
        'calendar': calendar,
        'prevmonth': prevmonth,
        'nextmonth': nextmonth
    }
    return render(request, 'calendar.html', context)

def Calendar_Spec(request, month):
    calmonth = get_date(month)
    cal = Calendar(calmonth.year, calmonth.month)
    # Call the formatmonth method, which returns our calendar as a table
    html_cal = cal.formatmonth(withyear=True)
    calendar = mark_safe(html_cal)
    prevmonth =prev_month(calmonth)
    nextmonth = next_month(calmonth)
    context = {
        'calendar': calendar,
        'prevmonth': prevmonth,
        'nextmonth': nextmonth
    }
    return render(request, 'calendar.html', context)


# based on the date it gets the first day of the month provided in the urls
# or provides you the date of today

def get_date(req_day):
    year, month = (int(x) for x in req_day.split('-'))
    return date(year, month, day = 1)

def prev_month(d):
    # get first day of first selected month
    # d is a date object from datetime module
    firstday = d.replace(day=1)
    # Get the day before the first day of the month
    # use timedelta
    prevmonth = firstday - timedelta(days = 1)
    month = str(prevmonth.year) + "-" + str(prevmonth.month)
    return month

def next_month(d):
    # same idea in reverse. get last day in month than add 1 timedelta
    # because each month has different number of days (particularly feb
    last = d.replace(day=28)
    nextmonth = last + timedelta(days = 4)
    month =  str(nextmonth.year) + "-" + str(nextmonth.month)
    return month
