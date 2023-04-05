from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import get_object_or_404

from taggit.managers import TaggableManager
from django_quill.fields import QuillField
# from tinymce import models as tinymce_models

from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse('board_app:category_list', args=[self.slug])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Post(models.Model):
    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    category_options = Category.objects.all().values_list('name', 'name')
    # # # category_options.sorted()
    category_list = []

    for item in category_options:
        category_list.append(item)

    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='post_pics')
    content = QuillField(null=True)
    # content = models.TextField(null=True)

    slug = models.SlugField(max_length=250, unique=True)
    date_posted = models.DateTimeField(default=timezone.now, editable=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author")
    status = models.CharField(max_length=10, choices=options, default="draft")
    # category = models.CharField(max_length=100, blank=True,)
    category = models.CharField(
        Category, max_length=100, choices=category_list,
        default='general')

    like = models.ManyToManyField(User, related_name="posts")
    tags = TaggableManager()

    class Meta:
        ordering = ('-date_posted',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def get_like_url(self):
        return reverse('posts:post_detail', kwargs={'slug': self.slug})

    def get_api_like_url(self):
        return reverse('post:api_like_post', kwargs={'slug': self.slug})

    def category_name(self):
        all = []
        for a in self.category.all():
            all.append(str(a))
        return "; ".join(all)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    # content = models.TextField(null=True)
    content = QuillField(null=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now, editable=False)
    status = models.BooleanField(default="True")

    class Meta:
        ordering = ('-date_posted',)

    def __str__(self):
        return f"comment by {self.author}"

    def get_absolute_url(self):
        return reverse('comment-detail', kwargs={'pk': self.pk})
