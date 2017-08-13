from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, JsonResponse
from todo.models import todo
from django.db.models import Case, Value, When
import datetime
import json
from django.core import serializers


def all_todo(request):
    add = request.POST.get('add', False)
    # get('click', False):  # check if called by click
    if request.method == 'POST' and add:
        title = request.POST.get('title')
        description = request.POST.get('description')
        new_todo = todo(title=title, description=description, done=False)
        new_todo.save()
        # todos = todo.objects.all()
        todos_json = serializers.serialize('json', [new_todo])
        # return JsonResponse({'todos': list(todos)})
        print(todos_json)
        return HttpResponse(todos_json, content_type='application/json')

    # print(request.method)
    print(request.POST)
    if request.method == "POST" and request.POST.get("check", False):
        print("POST og check")
        titles = request.POST.getlist('titles[]', False)
        print(titles)
        for title in titles:
            todo.objects.filter(title=title).update(
                done=Case(When(done=True, then=Value(False)),
                          default=Value(True)))

            #obj, created = todo.objects.update_or_create(
            #    title=title, defaults={'done': True})
            #print(created)
            # t.save(update_fields=['done'])
        print(titles)
        return HttpResponse()

    todos_undone = todo.objects.filter(done=False)
    todos_done = todo.objects.filter(done=True)
    # print(todos.values())
    now = datetime.datetime.now()
    return render(request, 'index.html', {'todos_undone': todos_undone, 'todos_done': todos_done})
# Create your views here.
