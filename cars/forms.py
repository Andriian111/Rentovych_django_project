from django import forms
from django.forms import TextInput

from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ("mark_car", "year_create", "number_car", 
        "type_fuel_engine",
         "kilometrage_car", "photo_car")
        # widgets = {
        #     "mark_car": TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': "Enter mark of car"
        #     }),
        #     "year_create": TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': "Enter year of creation car"
        #     }),
        #     "number_car": TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': "Enter number_car of car"
        #     }),
        #     "type_fuel_engine": TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': "Specify the type of  fuel engine of car"
        #     }),
        #     "kilometrage_car": TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': "Enter  mileage of the car"
        #     }),
        #     "photo_car": TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': "Enter photo of car"
        #     })
        # }

    # def __init__(self, *args, **kwargs):
    #     super(CarForm, self).__init__( *args, **kwargs)
    #     self.fields['mark_car'].empty_label= "Select"
    #     self.fields["kilometrage_car"].requried = False