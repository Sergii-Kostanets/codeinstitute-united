from .models import Game
from django import forms


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'slug', 'excerpt', 'content', 'featured_image', 'status']
