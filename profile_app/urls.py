from django.urls import path
from . import views

# from profile_app import views

from profile_app .views import ProfileListView

urlpatterns = [
    path('edit/', views.edit_profile, name='edit_profile'),
    path('<str:username>/', ProfileListView.as_view(), name='profile'),
]
