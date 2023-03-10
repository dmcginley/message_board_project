from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render

# from django.contrib import messages
from django.views.generic import ListView
from board_app.models import Post
# from urllib import request
# from django.urls import reverse


from django.contrib.auth.models import User
# from profile_app.models import Profile
from .forms import (
    ProfileUpdateForm,
    UserUpdateForm,
)


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


# def edit_profile(request):
#     # pass
#     if request.method == 'POST':
#         user_form = ProfileUpdateForm(request.POST, instance=request.user)
#         # form1 = UpdateProfileForm(request.POST, instance=request.user)
#         if user_form.is_valid:
#             user_form.save()
#             # form1.save()
#             return redirect('profile')
#     # else:
#         # user_form = ProfileUpdateForm(instance=request.user)
#         # form1 = UpdateProfileForm(instance=request.user)
#         context = {
#             'user_form': user_form,
#             # 'form1': form1,
#         }
#         return render(request, 'profile_app/edit_profile.html', context)


def edit_profile(request):
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(
            #     request, f'Account update successful')
            # return redirect('user-posts', request.user.username)
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'profile_app/edit_profile.html', context)
