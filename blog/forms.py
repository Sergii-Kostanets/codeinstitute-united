from .models import Post
from .models import Comment
from django import forms
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content', 'featured_image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
