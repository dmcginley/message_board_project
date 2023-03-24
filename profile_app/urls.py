from django.urls import path
from . import views

# from profile_app import views

from profile_app .views import (
    ProfileListView,
    CrmListView,
    CrmUserView,
    UserDeleteView
)

from board_app .views import (
    CategoryCreateView,
    CategoryDeleteView,
)


urlpatterns = [
    path('edit/', views.edit_profile, name='edit_profile'),
    path('crm/', CrmListView.as_view(), name='crm'),
    path('<str:username>/', ProfileListView.as_view(), name='profile'),
    path('crm/<slug:slug>', CrmUserView.as_view(), name='user_crm'),
    path('<slug:slug>/crm/delete/',
         UserDeleteView.as_view(), name='delete_user'),
    path('room/create/', CategoryCreateView.as_view(),
         name='create_category'),
    path('room/<slug:slug>/delete/', CategoryDeleteView.as_view(),
         name='delete_category'),
]
