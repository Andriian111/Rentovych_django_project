from django.shortcuts import render



def mainPage(requst):
    return render(requst, "main/base.html")
