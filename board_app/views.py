# from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
# from urllib import request


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from taggit.models import TaggedItem


from .models import Post, Comment
from django.views.generic import (
    ListView, CreateView,
    DetailView, UpdateView,
    DeleteView
)
from .forms import PostForm, CommentForm, PostSearchForm


class PostListView(ListView):
    """ The homepage """

    model = Post
    context_object_name = 'posts'
    paginate_by = 6
    template_name = "board_app/index.html"

    # def get_template_names(self):
    #     if self.request.htmx:
    #         return 'board_app/components/post_list_elements.html'
    #     return 'board_app/index.html'


# class PostDetailView(DetailView):
#     model = Post


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_items"] = self.object.tags.similar_objects()[:4]

        return context

# --------------------------------
#   post views
# --------------------------------


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


# --------------------------------
#   comment views
# --------------------------------
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


# --------------------------------
#   search views
# --------------------------------
class PostSearchView(ListView):
    model = Post
    # min_length = 3
    paginate_by = 10
    context_object_name = "posts"
    form_class = PostSearchForm
    template_name = 'board_app/search.html'

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            return Post.objects.filter(title__icontains=form.cleaned_data['q'])
        return Post.objects.all()


# --------------------------------
#   tag views
# --------------------------------
class TagListView(ListView):
    model = Post
    paginate_by = 2

    context_object_name = "posts"

    template_name = "board_app/tag_page.html"

    def get_queryset(self):
        return Post.objects.filter(tags__slug__in=[self.kwargs["tag"]])

    # def get_template_names(self):
    #     # if self.request.htmx:
    #     #     return 'blog_app/components/post_list_elements_tag.html'
    #     # return 'board_app/tag_page.html'

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context["tag"] = self.kwargs["tag"]
        return context


# class SimilarPosts(
    # model = Post
    # all_tags = instance.tags.all()

    # similar_posts = instance.tags.similar_objects()

    # def sim_post(request, pk):
    # sim_post = get_object_or_404(Post, pk=pk)
    # similar_posts = sim_post.tags.similar_objects()[:5]
    # context = {
    #     'sim_post':sim_post,
    #     'similar_posts':similar_posts
    # }
    # return render(request, 'similar_posts.html', context)
# )


# --------------------------------
#   error views: 400, 403, 404, & 500
# --------------------------------
def bad_request(request, *args, **argv):
    return render(request, 'board_app/error400.html', status=400)


def access_denied(request,  *args, **argv):
    return render(request, 'board_app/error403.html', status=403)


def page_not_found_view(request, *args, **argv):
    return render(request, 'board_app/error404.html', status=404)


def handler500(request,  *args, **argv):
    return render(request, 'board_app/error500.html', status=500)
