from django.shortcuts import render, get_object_or_404, redirect

from blog.models import Employee
from .models import Visit
from .forms import VisitForm


def show_visit(request):
    return render(request, 'visits/add_visit.html')


def visit_list(request):
    visits = Visit.objects.all()
    return render(request, 'visits/visit_list.html', {'visits': visits})


def visit_detail(request, pk):
    visit = get_object_or_404(Visit, pk=pk)
    return render(request, 'visits/visit_detail.html', {'visit': visit})


def visit_new(request):
    if request.method == "POST":
        form = VisitForm(request.POST)
        if form.is_valid():
            visit = form.save()
            return redirect('/visit/')
    else:
        form = VisitForm()
    return render(request, 'visits/add_visit.html', {'form': form})


def visit_edit(request, id):
    visit = Visit.objects.get(id=id)
    if request.method == "POST":
        form = VisitForm(request.POST, instance=visit)
        if form.is_valid():
            form.save()
            return redirect('/visit/')
    else:
        form = VisitForm(instance=visit)
    return render(request, 'visits/visit_edit.html', {'form': form, 'visit': visit})


def visit_delete(request, id):
    visit = Visit.objects.get(id=id)
    visit.delete()
    return redirect('/visit')

