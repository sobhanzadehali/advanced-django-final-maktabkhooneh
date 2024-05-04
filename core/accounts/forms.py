from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models.user import SubUser, CustomUser

class SubForm(forms.ModelForm):
    class Meta:
        model = SubUser
        fields = ('email',)


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)