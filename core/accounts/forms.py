from django import forms
from accounts.models.user import SubUser

class SubForm(forms.ModelForm):
    class Meta:
        model = SubUser
        fields = ('email',)