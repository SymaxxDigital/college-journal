from django.urls import path
from .views import ProfileView, ProfileCreateView, ProfileUpdateView

app_name = 'student_profile'

urlpatterns = [
    path("", ProfileView.as_view(), name="profile"),
    path("add/", ProfileCreateView.as_view(), name="profile_add"),
    path("edit/<uuid:pk>/", ProfileUpdateView.as_view(), name="profile_edit"),
]
