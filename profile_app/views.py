from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView
# from urllib import request


from board_app.models import Post
from profile_app.models import Profile


class ProfileListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'profile_app/profile_page.html'
    context_object_name = 'posts'

# TODO: get profile posts working
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

    # insert an extra variable into the context for this list view

    def get_context_data(self, **kwargs):
        context = super(ProfileListView, self).get_context_data(**kwargs)
        username = self.kwargs.get('username')
        print(f"loading user? {username}")

        user = User.objects.filter(username=username).first()

        print(user)
        context.update({
            'user': user
        })
        return context
