from django.shortcuts import render
from .models import HomeProduct, MonthProduct, FeaturedProduct, Contact, Subscribe

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
    return render(request, 'contact.html')


def shop(request):
    return render(request, 'shop.html')


def shop_single(request):
    return render(request, 'shop_single.html')


def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        Subscribe.objects.create(
            email=email
        )
    return render(request, 'base.html')
