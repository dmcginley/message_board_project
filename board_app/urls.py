from django.urls import path
from . import views

from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentDeleteView,
    TagListView,
    PostSearchView,
    #     LikePostView,
    # LikePostToggleView,
)


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('room/<slug:category_slug>/', views.category_list,
         name='category_list'),
    path('room/<slug:category_slug>/', views.category_snap_list,
         name='category_snap'),
    path('search/', PostSearchView.as_view(), name='search'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    # path('post/<slug:slug>/like', LikePostView.as_view(), name='like_post'),
    #     path('api/post/like', LikePostView.as_view(), name='api_like_post'),
    #     post
    path('add-post/', PostCreateView.as_view(), name='add_post'),
    path('edit-post/<slug:slug>/', PostUpdateView.as_view(), name='edit_post'),
    path('delete-post/<slug:slug>/', PostDeleteView.as_view(),
         name='delete_post'),
    #     comment
    path('add-comment/<int:pk>/', CommentCreateView.as_view(),
         name='add_comment'),
    path('post/<slug:slug>/comment/<int:pk>/delete', CommentDeleteView.as_view(),
         name='delete_comment'),



    path('tag/<slug:tag>/', TagListView.as_view(), name='tag_post_page'),
]
