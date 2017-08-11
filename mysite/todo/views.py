from django.shortcuts import render
from models import todo
import datetime


def all_todo(request):
    todos = todo.objects.all()
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})
# Create your views here.
