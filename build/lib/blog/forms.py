# In your blog/forms.py file

from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'heading', 'content', 'image', 'publisher']


