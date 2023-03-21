from django.urls import path
from . import views

# from profile_app import views

from profile_app .views import (
    ProfileListView,
    CrmListView,
    CrmUserView,
    UserDeleteView
)
urlpatterns = [
    path('edit/', views.edit_profile, name='edit_profile'),
    path('crm/', CrmListView.as_view(), name='crm'),
    path('<str:username>/', ProfileListView.as_view(), name='profile'),
    path('crm/<slug:slug>', CrmUserView.as_view(), name='user_crm'),
    path('<slug:slug>/crm/delete/',
         UserDeleteView.as_view(), name='delete_user'),
]
