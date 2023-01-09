from django.contrib.auth.models import User
from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post','user']