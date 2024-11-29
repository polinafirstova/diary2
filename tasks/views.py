from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def task_list(request):
    status_filter = request.GET.get('status', 'all')
    if status_filter == 'completed':
        tasks = Task.objects.filter(status='completed')
    elif status_filter == 'in_progress':
        tasks = Task.objects.filter(status='in_progress')
    elif status_filter == 'pending':
        tasks = Task.objects.filter(status='pending')
    else:
        tasks = Task.objects.exclude(status='completed')

    return render(request, 'task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        task = Task(title=title, description=description)
        task.save()
        return redirect('task_list')
    return render(request, 'add_task.html')


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.status = request.POST['status']
        task.save()
        return redirect('task_list')
    return render(request, 'edit_task.html', {'task': task})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
