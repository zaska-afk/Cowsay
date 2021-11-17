from django import forms
from cowsay_app.models import Cowsay


class CowsayForm(forms.ModelForm):
    class Meta:
        model = Cowsay
        fields = '__all__'