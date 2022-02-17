from django import forms

from .models import Customer_Reg, Ecom_Chair, Ecom_Dining, Ecom_Bed, Ecom_Armchairs


class customer_regform(forms.ModelForm):

    class Meta:
        model=Customer_Reg
        fields="__all__"


class sofa_form(forms.ModelForm):

    class Meta:
        model=Ecom_Chair
        fields="__all__"

class dining_form(forms.ModelForm):

    class Meta:
        model=Ecom_Dining
        fields="__all__"


class bed_form(forms.ModelForm):
    class Meta:
        model=Ecom_Bed
        fields='__all__'

class armchair_form(forms.ModelForm):
    class Meta:
        model=Ecom_Armchairs
        fields='__all__'