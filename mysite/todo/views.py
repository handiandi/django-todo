from django.shortcuts import render
from django.views.decorators.csrf
from django.http import HttpResponse
from todo.models import todo
from django.db.models import Case, Value, When
from django.core import serializers


def all_todo(request):
    add = request.POST.get('add', False)
    if request.method == 'POST' and add:
        title = request.POST.get('title')
        description = request.POST.get('description')
        new_todo = todo(title=title, description=description, done=False)
        new_todo.save()
        todos_json = serializers.serialize('json', [new_todo])
        return HttpResponse(todos_json, content_type='application/json')

    if request.method == "POST" and request.POST.get("check", False):
        titles = request.POST.getlist('titles[]', False)
        for title in titles:
            todo.objects.filter(title=title).update(
                done=Case(When(done=True, then=Value(False)),
                          default=Value(True)))
        return HttpResponse()

    todos_undone = todo.objects.filter(done=False)
    todos_done = todo.objects.filter(done=True)
    return render(request, 'index.html', {'todos_undone': todos_undone,
                                          'todos_done': todos_done})
