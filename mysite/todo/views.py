from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, JsonResponse
from todo.models import todo
import datetime, json
from django.core import serializers

@csrf_protect
def all_todo(request):
    add = request.POST.get('add', False)
    if request.method == 'POST' and add:  # get('click', False):  # check if called by click
        title = request.POST.get('title')
        description = request.POST.get('description')
        new_todo = todo(title=title, description=description, done=False)
        new_todo.save()
        # todos = todo.objects.all()
        todos_json = serializers.serialize('json', [new_todo])
        # return JsonResponse({'todos': list(todos)})
        print(todos_json)
        return HttpResponse(todos_json, content_type='application/json')

    if request.method == "PUT" and request.PUT.get("check", False):
        print("PUT!")

    todos = todo.objects.all()
    now = datetime.datetime.now()
    return render(request, 'index.html', {'todos': todos})
# Create your views here.
