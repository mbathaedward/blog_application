from django import forms
from .models import Post

class PostCreationform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','author', 'content','date_created']
