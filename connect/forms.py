from django import forms
from .models import Game
from django_summernote.widgets import SummernoteWidget
from bs4 import BeautifulSoup


class GameForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())
    
    class Meta:
        model = Game
        fields = ('title', 'slug', 'platform', 'excerpt', 'content', 'featured_image')

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if content:
            # Remove HTML tags and check if the resulting content is empty
            stripped_content = ''.join(BeautifulSoup(content).findAll(text=True))
            if not stripped_content.strip():
                raise forms.ValidationError("Content field is required")
        return content

