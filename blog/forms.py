from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post    # uses Post model from blog.models.py
        fields = ('title', 'text',) # only title and text would show up
