from django.forms import ModelForm

from coffees.models import Coffee


class CoffeeForm(ModelForm):
    class Meta:
        model = Coffee
        fields = '__all__'
