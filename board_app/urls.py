from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    CommentCreateView,
    PostUpdateView,
    PostDeleteView,
    TagListView,

    # PostSearchView,
)


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),

    path('add-post/', PostCreateView.as_view(), name='add_post'),

    path('edit-post/<slug:slug>/', PostUpdateView.as_view(), name='edit_post'),
    path('delete-post/<slug:slug>/', PostDeleteView.as_view(),
         name='delete_post'),
    path('add-comment/<int:pk>/', CommentCreateView.as_view(),
         name='add_comment'),
    path('tag/<slug:tag>/', TagListView.as_view(), name='tag_post_page'),

]
