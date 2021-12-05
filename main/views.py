from django.shortcuts import render
from .models import Books


def mainPage(requst):
    books = Books.objects.all()
    return render(requst, "main/base.html", {'tittle': 'Main page site', 'books':books})
