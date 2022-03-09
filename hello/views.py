from django.shortcuts import render
from .models import Contact


# Create your views here.


def home(request):
    return render(request, 'hello/home.html')


def about(request):
    return render(request, 'hello/about.html')


def portfolio(request):
    return render(request, 'hello/portfolio.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')

        contact_form = Contact(name=name, email=email, number=number, message=message)
        contact_form.save()

        return render(request, 'hello/thank you.html')

    else:
        return render(request, 'hello/contact.html')
