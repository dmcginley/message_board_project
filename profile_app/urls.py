from django.urls import path

# from profile_app import views

from profile_app .views import ProfileListView

urlpatterns = [
    path('', ProfileListView.as_view(), name='profile'),
]
