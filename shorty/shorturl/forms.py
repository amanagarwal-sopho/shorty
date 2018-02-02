from django import forms
from .models import URLEntry

class URLForm(forms.ModelForm):
    class Meta:
        model = URLEntry
        fields = ['url']
        


