from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    CommentCreateView,
    PostUpdateView,
    PostDeleteView,

    # PostSearchView,
    # TagListView,
)


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('add-post/', PostCreateView.as_view(), name='add_post'),

    path('add-comment/<int:pk>/', CommentCreateView.as_view(),
         name='add_comment'),

]
