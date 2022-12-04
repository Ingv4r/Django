from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('id')
    task = {
        'title': 'Главная страница сайта',
        'tasks': tasks
    }
    return render(request, 'main/index.html', task)


def about(request):
    return render(request, 'main/about.html')


def filling_form(request):
    return render(request, 'main/filling_form.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверная форма'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
