# from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post, Comment
from django.views.generic import (
    ListView, CreateView,
    DetailView, UpdateView,
    DeleteView
)
from .forms import PostForm, CommentForm


class PostListView(ListView):
    """ The homepage """

    model = Post
    context_object_name = 'posts'
    template_name = "board_app/index.html"

    # def get_template_names(self):
    #     if self.request.htmx:
    #         return 'blog_app/components/post_list_elements.html'
    #     return 'blog_app/index.html'


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "board_app/add_post.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post

    form_class = PostForm
    template_name = 'board_app/edit_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'board_app/delete_post.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'board_app/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # return 'blog_app/index.html'

        return reverse('post_detail', kwargs={'slug': self.object.post.slug})


# ------------------------------
#   error views: 400, 403, 404, & 500
# ------------------------------
def bad_request(request, *args, **argv):
    return render(request, 'board_app/error400.html', status=400)


def access_denied(request,  *args, **argv):
    return render(request, 'board_app/error403.html', status=403)


def page_not_found_view(request, *args, **argv):
    return render(request, 'board_app/error404.html', status=404)


def handler500(request,  *args, **argv):
    return render(request, 'board_app/error500.html', status=500)
