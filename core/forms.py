from django import forms
from .models import Subscribers

class AddEmailToSubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ('email',)