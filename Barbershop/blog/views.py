from django.shortcuts import render
from .models import Service, Subscribe, Appointment, Position, Barber, Testimonial, Contact


def index(request):
    return render(request, 'index.html')


def services(request):
    service_list = Service.objects.all()
    mid = len(service_list) // 2
    services_1 = service_list[:mid]
    services_2 = service_list[mid:]
    context = {
        'services_1': services_1,
        'services_2': services_2
    }
    return render(request, 'services.html', context=context)


def about(request):
    return render(request, 'about.html')


def barbers(request):
    barber = Barber.objects.all()
    return render(request, 'barbers.html', {'barbers': barber})


def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        datetime = request.POST['datetime']
        comment = request.POST['comments']
        Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            datetime=datetime,
            comment=comment
        )
    return render(request, 'contact.html')


def appointment(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        datetime = request.POST['datetime']
        comment = request.POST['comments']
        Appointment.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            datetime=datetime,
            comment=comment
        )
    return render(request, 'appointment.html')
