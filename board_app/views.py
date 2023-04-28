# from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.models import User
# from rest_framework import authentication, permissions
# from rest_framework.response import Response
# from rest_framework.views import APIView

from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.contrib import messages

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


# from django.contrib import messages
# from urllib import request
from django.utils.text import slugify

from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import F


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
# from taggit.models import TaggedItem


from .models import Post, Comment, Category
from profile_app .models import Profile

from django.views.generic import (
    ListView, CreateView,
    UpdateView,
    DeleteView,
    RedirectView,
    View,
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

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def form_valid(self, form):
        messages.success(self.request, 'Post updated successfully')
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'board_app/delete_post.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        # if self.request.user == post.author:
        if self.request.user == post.author or self.request.user.is_superuser:

            return True
        return False

    def form_valid(self, form):
        messages.success(self.request, 'Post deleted.')
        return super().form_valid(form)


# TODO: not working,
# --------------------------------
#   like post views
# --------------------------------


#         return JsonResponse()

@login_required
@require_POST
def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    likes_count = post.like.count()
    likes = post.like.all()
    if request.user in likes:
        post.like.remove(request.user)
        likes_count = likes.count() - 1

        return HttpResponse(
            f'<span class="likes-count has-text-grey ml-1">{likes_count} like</span>'
        )
    else:
        post.like.add(request.user)
        likes_count = likes.count() + 1

        return HttpResponse(f'<span class="likes-count has-text-grey ml-1"> {likes_count} unlike </span >')

    #     # return redirect('/')
    # # post.like.add(request.user)
    #     return HttpResponseRedirect(reverse('post_detail', slug=slug))
    # if request.user.is_authenticated:
    #     post = get_object_or_404(Post, slug=slug)
    #     if post.like.filter(id=request.user.id):
    #         post.like.remove(request.user)
    #     else:
    #         post.like.add(request.user)
    #     return HttpResponseRedirect(reverse('post_detail', slug=slug))
    # else:
    #     return HttpResponse('You need to be logged in to like a post.')
    # if request.method == 'POST':
    #     # Perform like action
    #     return JsonResponse({'status': 'liked'})
    # class LikePostView(RedirectView):
    #     # model = Post
    #     # template_name = 'board_app/delete_post.html'
    #     def get_redirect_url(self, *args, **kwargs):
    #         slug = self.kwargs.get("slug")
    #         print(slug)
    #         obj = get_object_or_404(Post, slug=slug)
    #         url_ = obj.get_absolute_url()
    #         user = self.request.user
    #         if user.is_authenticated:
    #             if user in obj.like.all():
    #                 obj.like.remove(user)
    #             else:
    #                 obj.like.add(user)
    #             obj.save()
    #             return url_
    # return reverse('post_detail', kwargs={'slug': slug})
    # class LikePostView(APIView):
    #     authentication_classes = (authentication.SessionAuthentication,)
    #     permission_classes = (permissions.IsAuthenticated,)
    #     def get(self, request, slug=None, format=None):
    #         slug = self.kwargs.get("slug")
    #         obj = get_object_or_404(Post, slug=slug)
    #         url_ = obj.get_absolute_url()
    #         user = self.request.user
    #         updated = False
    #         liked = False
    #         if user.is_authenticated():
    #             if user in obj.likes.all():
    #                 liked = False
    #                 obj.likes.remove(user)
    #             else:
    #                 liked = True
    #                 obj.likes.add(user)
    #             updated = True
    #         data = {
    #             "updated": updated,
    #             "liked": liked
    #         }
    #         return Response(data)
    # class LikePostView(RedirectView):
    #     model = Post
    #     def get_redirect_url(self, *args, **kwargs):
    #         slug = self.kwargs.get("slug")
    #         print(slug)
    #         obj = get_object_or_404(Post, slug=slug)
    #         # url_ = obj.get_absolute_url()
    #         user = self.request.user
    #         if user.is_authenticated:
    #             if user in obj.like.all():
    #                 obj.like.remove(user)
    #             else:
    #                 obj.like.add(user)
    #             obj.save()
    #             # return url_
    #             return reverse('post_detail', kwargs={'slug': slug})
    # -------------------------------------------------------------------------
    #   category views
    # -------------------------------------------------------------------------
category_options = Category.objects.all().values_list('name', 'name')
category_list = []

for item in category_options:
    category_list.append(item)


def categories(request):

    return {
        'categories': Category.objects.all().order_by(
            'name')
    }


def category_list(request, category_slug):

    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category)

    page_title = category

    context = {
        'posts': posts,
        'category': category,
        'page_title': page_title,
    }

    return render(request, 'board_app/category_list.html', context)


# TODO: fix list
def category_snap_list(request, category_slug):

    categories = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(categories=categories).order_by('-id')[:3]

    context = {
        'posts': posts,
        'categories': categories,
    }

    # categories = Category.objects.prefetch_related('post_set').all()
    return render(request, 'board_app/components/category_snip.html', context)


class CategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Category
    fields = ['name']
    template_name = 'board_app/create_category.html'
    success_url = reverse_lazy('crm')

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        if Category.objects.filter(name=form.cleaned_data['name']).exists():
            messages.error(self.request, 'Room already exists.')
            return self.form_invalid(form)

        else:
            messages.success(
                self.request, 'Room created.')

            return super().form_valid(form)


class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    template_name = 'board_app/delete_category.html'
    # success_url = '/'
    success_url = reverse_lazy('crm')
    # pk_url_kwarg = 'slug'
    slug_field = 'slug'

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        messages.success(self.request, f'Room {self.kwargs["slug"]} deleted.')

        return super().form_valid(form)


# -------------------------------------------------------------------------
#   comment views
# -------------------------------------------------------------------------

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'board_app/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        messages.success(self.request, 'Comment added to post')
        return super().form_valid(form)

    def get_success_url(self):
        # return 'blog_app/index.html'

        return reverse('post_detail', kwargs={'slug': self.object.post.slug})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'board_app/delete_comment.html'
    # success_url = '/'

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

    def form_valid(self, form):
        messages.success(self.request, 'Comment deleted.')
        return super().form_valid(form)

    def get_success_url(self):

        # return reverse('post_detail', kwargs={'slug': self.object.post.slug})
        return reverse('post_detail', kwargs={'slug': self.object.post.slug})


# -------------------------------------------------------------------------
#   search views
# -------------------------------------------------------------------------
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


# -------------------------------------------------------------------------
#   tag views
# -------------------------------------------------------------------------
class TagListView(ListView):
    model = Post
    paginate_by = 2

    context_object_name = "posts"

    template_name = "board_app/tag_page.html"

    def get_queryset(self):
        return Post.objects.filter(tags__slug__in=[self.kwargs["tag"]])

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context["tag"] = self.kwargs["tag"]
        return context


class ModalCategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'board_app/add_category.html'
    success_url = reverse_lazy('crm')

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        if Category.objects.filter(name=form.cleaned_data['name']).exists():
            messages.error(self.request, 'Room already exists.')
            return self.form_invalid(form)

        else:
            messages.success(
                self.request, 'Room created.')

            return super().form_valid(form)


# -------------------------------------------------------------------------
#   error views: 400, 403, 404, & 500
# -------------------------------------------------------------------------

def bad_request(request, *args, **argv):
    return render(request, 'board_app/error400.html', status=400)


def access_denied(request,  *args, **argv):
    return render(request, 'board_app/error403.html', status=403)


def page_not_found_view(request, *args, **argv):
    return render(request, 'board_app/error404.html', status=404)


def handler500(request,  *args, **argv):
    return render(request, 'board_app/error500.html', status=500)
