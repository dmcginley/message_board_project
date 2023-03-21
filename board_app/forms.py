from django import forms
from django_quill.forms import QuillFormField

from taggit.forms import TagWidget
from django.contrib.auth.models import User
from importlib.resources import contents

from .models import Post, Comment, Category
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title',
                  'subtitle', 'category', 'content', 'status', 'tags']

        labels = {
            "title":  "title",
            "subtitle": "subtitle",
            "category": "category",
            "status": "status",
            "tags": "tags",
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['input'].widget.attrs.update({'class': 'input'})
        # Widgets = {
        #     'category': forms.Select(attrs={'class': 'button'}),
        # }

        # def clean_tags(self):
        #     """
        #     Force all tags to lowercase.
        #     """
        #     tags = self.cleaned_data.get('tags', None)
        #     if tags:
        #         tags = [t.lower() for t in tags]

        #     return tags


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    # def save(self, *args, **kwargs):
    #     Comment.objects.rebuild()
    #     return super(CommentForm, self).save(*args, **kwargs)


class PostSearchForm(forms.Form):
    q = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['search'].widget.attrs.update({'class': 'input'})
