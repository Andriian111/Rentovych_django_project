from django.db import models


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(null=True, max_length=20, verbose_name="Ім'я", default="")
    last_name = models.CharField(null=True, max_length=20, verbose_name="Прізвище", default="")
    birthday = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Дата народження")
    address_registration = models.TextField(default="", max_length=200, verbose_name="Місце прописки ", help_text="Вкажи повну адресу місця прописки: Місто, вулиця, номер будинку і квартири, індекс ")
    address_lives = models.TextField(default="", max_length=500,verbose_name="Місце проживання", blank =True, help_text="Вкажи адресу місця проживання, якщо відрізняється від місця прописки")
    photo_passport = models.ImageField(default="", verbose_name="Фото паспорта",upload_to=None, height_field=None, width_field=None, max_length=100, help_text="Завантаж фото сторінки паспорта з твоїм актуальним фото")
    start_work = models.DateField(auto_now=True, auto_now_add=False)
    passport_information = models.CharField(default="", verbose_name="Паспорт", max_length=20, help_text="Вкажи: серію, номер паспорта та де і ким виданий")
    license_driver = models.CharField(default="", verbose_name="Водійське посвідчення",null=True, max_length=20, help_text="Вкажи номер водійського посвідчення")
    license_driver_data = models.DateField(verbose_name="Дата завершення терміну водійського посвідчення",auto_now=False, auto_now_add=False, help_text="Вкажи дату, до якої дійсне водійське посвідчення")
    photo_license_driver = models.ImageField(default="",verbose_name="Фото водійського посвідчення",upload_to=None, height_field=None, width_field=None, max_length=100, help_text="Завантаж фото водійського посвідчення")
    objects = models.Manager()
    

    def __str__(self):
        return self.first_name
    