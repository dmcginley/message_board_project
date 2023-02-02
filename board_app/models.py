from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from taggit.managers import TaggableManager

from django.utils.text import slugify


# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     class Meta:
#         verbose_name_plural = "categories"

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('/')


class Post(models.Model):
    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    content = models.TextField(null=True)
    # content = QuillField(null=True)
    slug = models.SlugField(max_length=250, unique=True)
    date_posted = models.DateTimeField(default=timezone.now, editable=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author")
    status = models.CharField(max_length=10, choices=options, default="draft")
    # category = models.CharField(max_length=100, default='general')
    tags = TaggableManager()

    class Meta:
        ordering = ('-date_posted',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now, editable=False)
    status = models.BooleanField(default="True")

    class Meta:
        ordering = ('-date_posted',)

    def __str__(self):
        return f"comment by {self.author}"
