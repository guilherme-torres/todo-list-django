from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import TaskForm
from .models import Task

def index(request):
    form = TaskForm()
    return render(request, 'tasks/index.html', {
        'form': form, 'tasks': Task.objects.all()
    })


def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            task = Task(description=description)
            task.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'tasks/index.html', {'form': form})
    return render(request, 'tasks/index.html', {'form': TaskForm()})


def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request):
    pass
