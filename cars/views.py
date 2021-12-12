from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm

def main_car(request):
    return render(request, 'cars/base_cars.html')

def cars_list(request):
    context = {"cars_list": Car.objects.all()}
    return render(request, "cars/cars_list.html", context)

def car_form(request):
    form = CarForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CarForm()
        return redirect('/cars/list')
    context = {'form': form}
    # if request.method == "GET":
    #     if id ==0:
    #         form = CarForm
    #     else:
    #         books = Car.objects.get(pk=id)
    #         form = CarForm(isinstance=books)
    # else:
    #     if id ==0:
    #         form = CarForm(request.POST)
    #     else:
    #         books = Car.objects.get(pk=id)
    #         form = CarForm(request.POST, isinstance=books)
    #         if form.is_vaid():
    #             form.save()
    #         return redirect('/cars/list')
    return render(request, "cars/car_form.html", context)

def car_delete(request, id):
    books = Car.objects.get(pk=id)
    books.delete()
    return redirect ('/book/list')