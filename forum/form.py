from django import forms
from .models import Forum

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['key_art', 'name', 'price', 'popularity', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'popularity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
