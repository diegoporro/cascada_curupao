from django.shortcuts import render
import datetime


def home(request):

    x = datetime.datetime.now()
    exp = int(x.year)-2012

    context = {
        "exp": exp,
    }
    return render(request, 'index.html', context)
