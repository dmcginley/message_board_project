from django import forms
from django_quill.forms import QuillFormField

from taggit.forms import TagWidget
from django.contrib.auth.models import User
from importlib.resources import contents

from .models import Post, Comment, Category
from django.contrib.auth.forms import UserCreationForm


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django import forms
from crispy_bulma.layout import UploadField
from crispy_bulma.forms import ImageField


class PostForm(forms.ModelForm):
    # content = QuillFormField()

    class Meta:
        model = Post
        fields = ['category', 'title', 'image',
                  'content', 'status', 'tags']

        # labels = {
        #     "title":  "title",
        #     "image":  "image",
        #     "category": "room",
        #     "status": "status",
        #     "tags": "tags",
        # }

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        # self.helper = FormHelper()

        # self.helper.layout = Layout(
        #     UploadField("image"),
        #     # UploadField("my_file"),
        # )
    # my_file = FileField(
    #     label="Upload your actual dog in .dog format",
    #     required=True
    # )

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
