from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'classe']
        widgets = {
            'classe': forms.Select(choices=Player.CLASS_CHOICES)
        }