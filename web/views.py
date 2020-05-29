from django.shortcuts import render
import datetime
from .forms import *
from .models import *
import smtplib
from django.core.mail import EmailMessage


def home(request):

    x = datetime.datetime.now()
    exp = int(x.year)-2012
    form = Contact(request.POST or None)

    if form.is_valid():
        context = {
            'form': form,
        }
        Nombre = form.cleaned_data.get("Nombre")
        Email = form.cleaned_data.get("Email")
        Telefono = form.cleaned_data.get("Telefono")
        Mensaje = form.cleaned_data.get("Mensaje")

        title = 'Cliente: ' + Nombre
        body = str(Nombre + ' ' + Email + ' ' + Telefono + ' ' + Mensaje + ' ' + str(x.year) + ' ©  · Cascada de Curupao')

        email = EmailMessage(title, body, to=['diegoporro25@gmail.com'])
        email.send()

        print(title, Nombre, Email, Telefono, Mensaje)

        form = Contact

    context = {
        "exp": exp,
        'form': form,
    }
    return render(request, 'index.html', context)
