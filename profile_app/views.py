from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


from board_app.models import Post


class ProfileListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'profile_app/profile_page.html'
    context_object_name = 'posts'
