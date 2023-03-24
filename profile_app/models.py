from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from board_app.models import Post


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    posts = models.ForeignKey(
        Post, related_name='user_posts', null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    image = models.ImageField(
        default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
