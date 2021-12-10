# Generated by Django 3.2.9 on 2021-12-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_employee_license_driver_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='address',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='photo',
        ),
        migrations.AddField(
            model_name='employee',
            name='address_lives',
            field=models.TextField(blank=True, default='', help_text='Вкажи адресу місця проживання, якщо відрізняється від місця прописки', max_length=500, verbose_name='Місце проживання'),
        ),
        migrations.AddField(
            model_name='employee',
            name='address_registration',
            field=models.TextField(default='', help_text='Вкажи повну адресу місця прописки: Місто, вулиця, номер будинку і квартири, індекс ', max_length=200, verbose_name='Місце прописки '),
        ),
        migrations.AddField(
            model_name='employee',
            name='photo_license_driver',
            field=models.ImageField(default='', help_text='Завантаж фото водійського посвідчення', upload_to=None, verbose_name='Фото водійського посвідчення'),
        ),
        migrations.AddField(
            model_name='employee',
            name='photo_passport',
            field=models.ImageField(default='', help_text='Завантаж фото сторінки паспорта з твоїм актуальним фото', upload_to=None, verbose_name='Фото паспорта'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='birthday',
            field=models.DateField(verbose_name='Дата народження'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(default='', max_length=20, null=True, verbose_name="Ім'я"),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(default='', max_length=20, null=True, verbose_name='Прізвище'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='license_driver',
            field=models.CharField(default='', help_text='Вкажи номер водійського посвідчення', max_length=20, null=True, verbose_name='Водійське посвідчення'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='license_driver_data',
            field=models.DateField(help_text='Вкажи дату, до якої дійсне водійське посвідчення', verbose_name='Дата завершення терміну водійського посвідчення'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='passport_information',
            field=models.CharField(default='', help_text='Вкажи: серію, номер паспорта та де і ким виданий', max_length=20, verbose_name='Паспорт'),
        ),
    ]
