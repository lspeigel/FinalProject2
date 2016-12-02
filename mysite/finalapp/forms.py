from django import forms
from .models import Input, AREA
from django.forms import ModelForm


class InputForm(forms.ModelForm):

    attrs = {'class ' : 'form-nav-control',
             'onchange ' : 'this.form.submit()'}

    area = forms.ChoiceField(choices = AREA, required=True,
                               widget=forms.Select(attrs = attrs))
    class Meta:

        model = Input
        fields = ['area']
