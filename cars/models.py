from django.db import models

class Car(models.Model):
    variants_fuel= [("disel","Дизель"), ("petrol","Бензин"), ("gas_petrol","Газ/бензин"), ("Electro","Електричний"), ("Petrol_electro","Бензин/електричний")]
    mark_car = models.CharField(max_length=20, default="", verbose_name="Марка машини")
    year_create = models.IntegerField(default=0, verbose_name="Рік виготовлення машини")
    number_car = models.CharField(max_length=20, default="", verbose_name="Номерний знак машини")
    type_fuel_engine = models.CharField(max_length=20,verbose_name="Тип двигуна", default=variants_fuel[1][0], choices=variants_fuel)
    kilometrage_car = models.IntegerField(default=0, verbose_name="Кілометраж")
    photo_car = models.ImageField(verbose_name="Фото машини", upload_to=None, height_field=None, width_field=None, max_length=100)
    objects = models.Manager()