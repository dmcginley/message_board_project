from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Count
from django.urls import reverse
from django.http import JsonResponse


from django.http import HttpResponseRedirect, HttpResponse

# from django.contrib import messages
from django.views.generic import (
    ListView, DetailView,
    DeleteView, CreateView,
)
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from django.views import generic
from django.contrib import messages


from board_app.models import Post, Comment, Category
# from urllib import request
# from django.urls import reverse


from django.contrib.auth.models import User
# from profile_app.models import Profile
from .forms import (
    ProfileUpdateForm,
    UserUpdateForm,
)


class ProfileListView(LoginRequiredMixin, ListView):
    model = User
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


def edit_profile(request):
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request, f'Profile update successful')
            return redirect('edit_profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'profile_app/edit_profile.html', context)


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    slug_field = 'username'

    template_name = 'profile_app/delete_user.html'

    success_url = '/profile/crm/'

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        messages.success(self.request, 'User deleted.')
        return super().form_valid(form)


class CrmListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    # model = None  # Set to None to allow for multiple models

    # def get_queryset(self):
    #     return {
    #         'user': User.objects.all(),
    #         'category': Category.objects.all(),
    #     }

    template_name = 'profile_app/crm_page.html'
    ordering = ('-date_joined',)  # or 'last_login'
    context_object_name = 'users'
    paginate_by = 8

    def test_func(self):
        return self.request.user.is_superuser

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context.update(self.get_queryset())
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all
        context['comments'] = Comment.objects.all
        context['user_count'] = User.objects.all

        return context


class CrmUserView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = User
    slug_field = 'username'

    template_name = 'profile_app/user_crm_page.html'

    def test_func(self):
        return self.request.user.is_superuser
    # add these methods to display posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author=self.object)
        context['comments'] = Comment.objects.filter(author=self.object)

        return context

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     qs = qs.filter(author=self.object)
    #     return qs
    # context_object_name = 'users'


def modal_content(request):
    return render(request, 'profile_app/modal_content.html')


class ModalCategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'profile_app/add_category.html'
    success_url = reverse_lazy('crm')

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        if Category.objects.filter(name=form.cleaned_data['name']).exists():
            messages.error(
                self.request, 'Room already exists.')
            return self.form_invalid(form)
            # return HttpResponse(status=204)

        else:
            messages.success(
                self.request, 'Room created.')

            return super().form_valid(form)
