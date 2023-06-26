from .models import Post
from .models import Comment
from django import forms
from django_summernote.widgets import SummernoteWidget
from bs4 import BeautifulSoup


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content', 'featured_image']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if content:
            # Remove HTML tags and check if the resulting content is empty
            stripped_content = ''.join(BeautifulSoup(content).findAll(text=True))
            if not stripped_content.strip():
                raise forms.ValidationError("Content field is required")
        return content
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if title:
            # Convert the title to lowercase
            title = title.lower()
            # Check if there are any other posts with the same lowercase title
            existing_posts = Post.objects.filter(title__iexact=title)
            if self.instance:
                existing_posts = existing_posts.exclude(pk=self.instance.pk)
            if existing_posts.exists():
                self.add_error('title', 'A post with this title already exists')
        return cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
