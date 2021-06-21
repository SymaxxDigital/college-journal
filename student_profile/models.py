import uuid
from django.db import models
from django.conf import settings
from django.urls import reverse



"""============================================Student==========================================="""

class PersonalInformation(models.Model):
    """ Student basic Information """
    SEX = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    other_name = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=20, choices=SEX, blank=True, null=True)
    other_gender = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self): # new
        return reverse('student_profile:profile_update', kwargs={'pk': str(self.pk)})

    class Meta:
        verbose_name_plural = "Personal Information"


class ContactDetail(models.Model):
    """ Student contact details """
    PHONE = (
        ("Home", "Home"),
        ("Mobile", "Mobile"),
    )

    related_field = models.ForeignKey(PersonalInformation, on_delete=models.CASCADE, null=True, blank=True)
    phone_option = models.CharField(max_length=20 ,choices=PHONE, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.phone_option} {self.phone_number}"


class Address(models.Model):
    related_field = models.ForeignKey(PersonalInformation, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    

    def __str__(self):
        return f"{self.address}"

    

class Demographic(models.Model):
    """ Student demographics  """
    RELIGION = (
        ("Christian", "Christian"),
        ("Hindu", "Hindu"),
        ("Muslim", "Muslim"),

    )

    RACE = (
        ("Black", "Black"),
        ("White", "White"),
        ("Asian", "Asian"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    religion = models.CharField(
        max_length=30, blank=True, null=True, choices=RELIGION)
    race = models.CharField(max_length=30, blank=True, null=True, choices=RACE)
    consent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.religion}"

    def get_absolute_url(self): # new
        return reverse('student_profile:demographic_update', kwargs={'pk': str(self.pk)})


class Language(models.Model):
    """ Student list of spoken languages """
    LANGUAGES = (
        ("English", "English"),
        ("Zulu", "Zulu")
    )
    
    PROFICIENCY = (
        ("First language", "First language"),
        ("Speak", "Speak"),
        ("Read", "Read"),
        ("Write", "Write"),
        ("Spoken at home", "Spoken at home"),
    )

    related_field = models.ForeignKey("Demographic", on_delete=models.CASCADE, null=True, blank=True)
    language = models.CharField(
        max_length=20, choices=LANGUAGES, blank=True, null=True)
    language_proficiency = models.CharField(max_length=50, blank=True, null=True, choices=PROFICIENCY)
    def __str__(self):
        return f"Proficient in {self.language}"


class Citizenship(models.Model):
    """ Student Citizenship """

    related_field = models.ForeignKey(Demographic, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


"""=======================================Family======================================"""


class Family(models.Model):

    RELATIONSHIP_STATUS = (
        ("Married", "Married"),
        ("Divorced", "Divorced"),
        ("Separated", "Separated"),
        ("Never Married", "Never Married"),
        ("Widowed", "Widowed"),
    )

    LIVING = (
        ("Parent1", "Parent1"),
        ("Parent2", "Parent2"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    relationship_status = models.CharField(
        max_length=20, blank=True, null=True, choices=RELATIONSHIP_STATUS)
    living_situation = models.CharField(
        max_length=20, blank=True, null=True, choices=LIVING)
    children = models.BooleanField()
    number_of_children = models.IntegerField()

    def __str__(self):
        return f"{self.relationship_status}"

    def get_absolute_url(self): # new
        return reverse('student_profile:family_update', kwargs={'pk': str(self.pk)})

    class Meta:
        verbose_name_plural = "Family"


class Parent(models.Model):
    PARENT = (
        ("Mother", "Mother"),
        ("Father", "Father"),
        ("Limited information", "I have limited information about this parent")
    )

    PREFIX = (
        ("Dr.", "Dr"),
        ("Ms.", "Ms."),
        ("Mr.", "Mr."),
        ("Mrs.", "Mrs."),
    )

    PHONE = (
        ("Mobile", "Mobile"),
        ("Home", "Home"),
        ("Work", "Work"),
        ("Other", "Other"),
    )
    
    related_parent = models.ForeignKey(Family, on_delete=models.CASCADE, null=True, blank=True)
    parent_type = models.CharField(
        max_length=100, blank=True, null=True, choices=PARENT)
    parent_status = models.BooleanField(verbose_name="Is parent living?")
    parent_prefix = models.CharField(
        max_length=10, blank=True, null=True, choices=PREFIX)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    birth_country = models.CharField(max_length=50, blank=True, null=True)
    preferred_email = models.EmailField(max_length=40, blank=True, null=True)
    preferred_phone = models.CharField(max_length=20, choices=PHONE)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    parent_address = models.CharField(max_length=50, blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True)
    education_level = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.parent_type}"


class Sibling(models.Model):
    RELATIONSHIP = (
        ("Brother", "Brother"),
        ("Sister", "Sister"),
    )

    related_parent = models.ForeignKey(Family, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    relationship = models.CharField(max_length=50, choices=RELATIONSHIP, blank=True, null=True)
    education_level = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name}"[0]


"""=======================================Education======================================"""


class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=200, blank=True, null=True)
    date_of_entry = models.DateField()
    school_type = models.BooleanField()
    graduation_status = models.BooleanField()
    graduation_date = models.DateField(null=True, blank=True)
    progression_status = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=250, blank=True, null=True)


    def __str__(self):
        return self.school_name

    class Meta:
        verbose_name_plural = "Education"

    def get_absolute_url(self): # new
        return reverse('student_profile:education_update', kwargs={'pk': str(self.pk)})

class School(models.Model):
    related_school = models.ForeignKey(Education, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=200, blank=True, null=True)
    date_started = models.DateField()
    date_finished = models.DateField()
    description = models.TextField(max_length=250, blank=True, null=True)


class FuturePlan(models.Model):
    related_school = models.ForeignKey(Education, on_delete=models.CASCADE)
    career_interest = models.CharField(max_length=50, blank=True, null=True)
    highest_degree = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(max_length=350, blank=True, null=True)

    def __str__(self):
        return self.career_interest


"""=======================================Activity======================================"""

class ActivityCheck(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity_interest = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return f"{self.activity_interest}"

    def get_absolute_url(self): # new
        return reverse('student_profile:activity_update', kwargs={'pk': str(self.pk)})

class Activity(models.Model):
    ACTIVITIES = (
        ('Art', 'Art'),
        ('Academic', 'Academic'),
    )

    PARTICIPATION = (
        ('During school year', 'During school year'),
        ('During school break', 'During school break'),
        ('All year', 'All year'),
    )
    related_field = models.ForeignKey(ActivityCheck, on_delete=models.CASCADE, null=True, blank=True)
    activity_type = models.CharField(max_length=200, blank=True, null=True, choices=ACTIVITIES)
    position = models.CharField(max_length=50, blank=True, null=True)
    organization = models.CharField(max_length=150, blank=True, null=True, verbose_name="Oraganization Name")
    accomplishment = models.CharField(max_length=200, blank=True, null=True)
    intension = models.BooleanField()
    hours_per_week = models.CharField(max_length=200, blank=True, null=True)
    weeks_per_year = models.CharField(max_length=200, blank=True, null=True)
    participation_time = models.CharField(max_length=50, blank=True, null=True, choices=PARTICIPATION)

    def __str__(self):
        return self.activity_type


"""=======================================Writing======================================"""

class PersonalEssay(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    consent = models.BooleanField(default=False)
    essay = models.TextField(max_length=800)

    def __str__(self):
        return f"{self.consent}"

    class Meta:
        verbose_name_plural = "Personal Essay"

    def get_absolute_url(self): # new
        return reverse('student_profile:personal_essay_update', kwargs={'pk': str(self.pk)})


class DisciplinaryHistory(models.Model):
    DISCIPLINED = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    related_field = models.ForeignKey(PersonalEssay, on_delete=models.CASCADE, null=True, blank=True)
    disciplinary = models.CharField(max_length=10, blank=True, null=True, choices=DISCIPLINED)


    def __str__(self):
        return self.disciplinary


class AdditionalInformation(models.Model):
    related_field = models.ForeignKey(PersonalEssay, on_delete=models.CASCADE, null=True, blank=True)
    any_disruptions = models.BooleanField()
    disruption = models.TextField(max_length=650, blank=True, null=True)
    any_curcumstance = models.BooleanField(default=False)
    circumstance = models.TextField(max_length=650, blank=True, null=True)

    def __str__(self):
        return f"Disruptions {self.any_disruptions}"

    