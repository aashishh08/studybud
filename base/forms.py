from django.forms import ModelForm
from .models import Room

# This is used to make form based on the models and the inputs mentioned in the model

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'