from django.urls import path
from .views import (
    ProfileView, 
    ProfileCreateView, 
    ProfileUpdateView, 
    DemographicListView,
    DemographicCreateView, 
    DemographicUpdateView,
    FamilyListView,
    FamilyCreateView,
    FamilyUpdateView,
    EducationListView,
    EducationCreateView,
    EducationUpdateView,
    ActivityListView,
    ActivityCreateView,
    ActivityUpdateView,
    PersonalessayListView,
    PersonalEssayCreateView,
    PersonalEssayUpdateView,


)

app_name = 'student_profile'

urlpatterns = [
    path("", ProfileView.as_view(), name="profile"),
    path("add/", ProfileCreateView.as_view(), name="profile_create"),
    path("edit/<uuid:pk>/", ProfileUpdateView.as_view(), name="profile_update"),
    path("demographics/", DemographicListView.as_view(), name="demographics"),
    path("demographic/add", DemographicCreateView.as_view(), name="demographic_create"),
    path("demographic/edit/<uuid:pk>", DemographicUpdateView.as_view(), name="demographic_update"),
    path("family", FamilyListView.as_view(), name="family"),
    path("family/add", FamilyCreateView.as_view(), name="family_create"),
    path("family/edit/<uuid:pk>", FamilyUpdateView.as_view(), name="family_update"),
    path("education", EducationListView.as_view(), name="education"),
    path("education/add", EducationCreateView.as_view(), name="education_create"),
    path("education/edit/<uuid:pk>", EducationUpdateView.as_view(), name="education_update"),
    path("activities/", ActivityListView.as_view(), name="activities"),
    path("activity/add", ActivityCreateView.as_view(), name="activity_create"),
    path("activity/edit/<uuid:pk>", ActivityUpdateView.as_view(), name="activity_update"),
    path("essays/", PersonalessayListView.as_view(), name="personalessays"),
    path("personal-essay/add", PersonalEssayCreateView.as_view(), name="personal_essay_create"),
    path("personal-essay/edit/<uuid:pk>", PersonalEssayUpdateView.as_view(), name="personal_essay_update"),
]
