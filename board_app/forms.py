from django import forms
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
<<<<<<< HEAD
=======
<<<<<<< Updated upstream
=======

>>>>>>> 5d874d51 (feat: add search bar to most pages)
        # def clean_tags(self):
        #     """
        #     Force all tags to lowercase.
        #     """
        #     tags = self.cleaned_data.get('tags', None)
        #     if tags:
        #         tags = [t.lower() for t in tags]

        #     return tags
<<<<<<< HEAD
=======
>>>>>>> Stashed changes
>>>>>>> 5d874d51 (feat: add search bar to most pages)


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
