from django import forms
from .models import Game
from django_summernote.widgets import SummernoteWidget


class GameForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())
    
    class Meta:
        model = Game
        fields = ('title', 'slug', 'excerpt', 'content', 'featured_image')
