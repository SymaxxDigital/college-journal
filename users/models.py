from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    is_first_year_student = models.BooleanField(default=False)
    is_transfare_student = models.BooleanField(default=False)
    is_education_proffessional = models.BooleanField(default=False)
    is_parent_or_adult = models.BooleanField(default=False)
    