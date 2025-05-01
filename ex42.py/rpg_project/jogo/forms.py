from django import forms
from .models import Personagem

class PersonagemForm(forms.ModelForm):
    class Meta:
        model = Personagem
        fields = ['nome', 'classe', 'forca', 'destreza', 'inteligencia', 'carisma']
