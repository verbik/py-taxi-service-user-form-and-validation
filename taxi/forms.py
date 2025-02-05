from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from taxi.models import Driver, Car


class DriverCreateForm(UserCreationForm):
    class Meta:
        model = Driver
        fields = UserCreationForm.Meta.fields + ("first_name",
                                                 "last_name",
                                                 "license_number",)


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ("license_number",)


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Car
        fields = "__all__"
