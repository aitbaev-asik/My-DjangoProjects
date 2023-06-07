from django.core.mail import send_mail
from django.shortcuts import render
from .models import Food, BookTable, Table, Response, Event, Category


def home(request):
    return render(request, 'home.html')


def menu_category(request, id):
    foods = Food.objects.filter(category__id=id)
    categories = Category.objects.all()
    context = {'foods': foods, 'categories': categories}
    return render(request, 'menu.html', context=context)


def menu(request):
    categories = Category.objects.all()
    foods = Food.objects.all()
    context = {
        'foods': foods, 'categories': categories
    }
    return render(request, 'menu.html', context=context)


def booktable(request):
    tables = Table.objects.all()
    if request.method == 'POST':
        table_id = request.POST.get('table')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        persons = request.POST.get('persons')
        message = request.POST.get('message')
        table = Table.objects.get(id=table_id)
        table.reserved = True
        table.save()
        BookTable.objects.create(
            table=table,
            name=name,
            email=email,
            phone=phone,
            date=date,
            persons=persons,
            message=message
        )
    return render(request, 'booktable.html', {'tables': tables})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        Response.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )
    return render(request, 'contact.html')


def event(request):
    events = Event.objects.all()
    return render(request, 'event.html', {'events': events})
