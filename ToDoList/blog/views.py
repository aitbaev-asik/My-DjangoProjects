from django.shortcuts import render, redirect

from blog.models import ToDo


def index(request):
    todo_list = ToDo.objects.all()
    context = {
        'todo_list': todo_list
    }
    return render(request, 'index.html', context=context)


def create_todo(request):
    if request.method == 'POST':
        print(request.POST)
        text = request.POST['text']
        ToDo.objects.create(text=text)
    return redirect('/')


def complete_todo(request, pk):
    todo = ToDo.objects.get(pk=pk)
    if todo.complete:
        todo.complete = False
    else:
        todo.complete = True
    todo.save()
    return redirect('/')


def delete_complete(request):
    ToDo.objects.filter(complete=True).delete()
    return redirect('/')


def delete_all(request):
    ToDo.objects.all().delete()
    return redirect('/')
