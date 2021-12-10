from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ("mark_car", "year_create", "number_car", 
        "type_fuel_engine", "kilometrage_car", "photo_car")
        labels = {
            'mark_car': "Марка машини ",
            'kilometrage_car': "Кілометраж"
        }

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__( *args, **kwargs)
        self.fields['mark_car'].empty_label= "Select"
        self.fields["kilometrage_car"].requried = False