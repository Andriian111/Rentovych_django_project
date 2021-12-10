from django.shortcuts import render
from .models import Employee


def mainPage(requst):
    books = Employee.objects.all()
    return render(requst, "main/base.html", {'tittle': 'Main page site', 'books':books})
