from django import forms
from taggit.forms import TagWidget
from django.contrib.auth.models import User
# from importlib.resources import contents

from .models import Post, Comment
# from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title',
                  'subtitle', 'content', 'status', 'tags']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['input'].widget.attrs.update({'class': 'input'})
        # Widgets = {
        #     'tags': forms.input(attrs={'class': 'input'}),
        # }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    # def save(self, *args, **kwargs):
    #     Comment.objects.rebuild()
    #     return super(CommentForm, self).save(*args, **kwargs)


class SearchForm(forms.Form):
    q = forms.CharField()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['search'].widget.attrs.update({'class': 'input'})
