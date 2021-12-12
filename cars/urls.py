from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_car,name="car_insert"),  
    path('list/', views.cars_list, name="cars_list"),
    path('update/', views.car_form,name="car_update"),
    path('delete/<int:id>/', views.car_delete,name="car_delete")
   
]