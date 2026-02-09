from django import forms
from .models import Post
#this form creates a form that matches the model/post allow users create or edit posts
class PostCreationform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','author', 'content','date_created','status','image']
