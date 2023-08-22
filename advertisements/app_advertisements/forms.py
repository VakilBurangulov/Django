from django.forms import ModelForm
from .models import Advertisements
from django import forms
from django.core.exceptions import ValidationError




class AdvertisementForm(ModelForm):
    def validate_even(self, value):
        if value[0] == '?':
            raise ValidationError(
                _("%(value)s начинается с ?"),
                params={"value": value},
            )


    class Meta:
        model = Advertisements
        fields = ['title', 'description', 'price', 'auction', 'image']
    title = forms.CharField(max_length=64,validators=[validate_even],
                            widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    description = forms.CharField(
                            widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
    price = forms.DecimalField(
                            widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
    auction = forms.BooleanField(required=False,
                            widget=forms.CheckboxInput(attrs={'class': 'form-control form-check-input'}))
    image = forms.ImageField(required=False,
                            widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))



