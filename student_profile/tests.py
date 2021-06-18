from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import (
    PersonalInformation, 
    ContactDetail, 
    Address, 
    Demographic, 
    Language, 
    Citizenship, 
    Family,
    Parent,
    Sibling,
    Education,
    School,
    FuturePlan,
    ActivityCheck,
    Activity,
    PersonalEssay,
    DisciplinaryHistory,
    AdditionalInformation,
)


class PersonalInformationTests(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user(  # new
            username='studentuser',
            email='studentuser@email.com',
            password='testpass123'
        )

        self.profile = PersonalInformation.objects.create(
            user = self.user,
            first_name="Maxx",
            middle_name="King",
            last_name="Moyo",
            nickname="Bk",
            other_name="Bkay",
            sex="Male",
            other_gender="Male",
            date_of_birth="1996-03-06",
        )

        self.contact = ContactDetail.objects.create(
            related_field = self.profile,
            phone_option = "Home",
            phone_number = "123 456 789"
        )

        self.address = Address.objects.create(
            related_field = self.profile,
            address = "home 123",
            city = "Pretoria",
            postal_code = "1234",
            country = "South Africa",
        )

        self.demographics = Demographic.objects.create(
            user = self.user,
            religion = "Christianity",
            race = "Black",
            consent = True,
        )
        
        self.language = Language.objects.create(
            related_field = self.demographics,
            language = "English",
            language_proficiency = "Speak",
        )

        self.citizenship = Citizenship.objects.create(
            related_field = self.demographics,
            name = "South African"
        )

        self.family = Family.objects.create(
            user = self.user,
            relationship_status = "Married",
            living_situation = "With both parents",
            children = False,
            number_of_children = 3,
        )

        self.parent = Parent.objects.create(
            related_parent = self.family,
            parent_type = "Mother",
            parent_status = True,
            parent_prefix = "Mrs.",
            first_name = "Mary",
            middle_name = "Samantha",
            last_name = "Jones",
            birth_country = "South Africa",
            preferred_email = "testmom@email.com",
            preferred_phone = "Mobile",
            phone_number = "123 456 789",
            parent_address = "Home 123",
            occupation = "Teacher",
            education_level = "College",
        )

        self.sibling = Sibling.objects.create(
            related_parent = self.family,
            first_name = "Philip",
            middle_name = "Sinothi",
            last_name = "Moyo",
            date_of_birth = "1990-08-20",
            relationship = "Brother",
            education_level = "University",
        )

        self.education = Education.objects.create(
            user = self.user,
            school_name = "Premier",
            date_of_entry = "2020-01-01",
            school_type = True,
            graduation_status = True,
            graduation_date = "2021-01-01",
            progression_status = "Graduate",
            description = "This text has to be here",
        )

        self.school = School.objects.create(
            related_school = self.education,
            school_name = "Green Gables",
            date_started = "2020-01-01",
            date_finished = "2021-01-01",
            description = "This text has to be here",
        )

        self.futureplan = FuturePlan.objects.create(
            related_school = self.education,
            career_interest = "Coding",
            highest_degree = "Masters",
            notes = "This text has to be here",
        )

        self.activitycheck = ActivityCheck.objects.create(
            user = self.user,
            activity_interest = True,
        )

        self.activity = Activity.objects.create(
            related_field = self.activitycheck,
            activity_type = "Art",
            position = "Leader",
            organization = "WHO",
            accomplishment = "Winner 2020",
            intension = True,
            hours_per_week = 30,
            weeks_per_year = 20,
            participation_time = "2hrs",
        )

        self.personalessay = PersonalEssay.objects.create(
            user = self.user,
            consent = True, 
            essay = "This text is supposed to be here",
        )

        self.discipline = DisciplinaryHistory.objects.create(
            related_field = self.personalessay,
            disciplinary = "Yes",
        )

        self.additionalinformation = AdditionalInformation.objects.create(
            related_field = self.personalessay,
            any_disruptions = True,
            disruption = "This text can be here",
            any_curcumstance = True,
            circumstance = "This text can be here",
        )

    def test_profile_information(self):
        self.assertEqual(f"{self.profile.user}", "studentuser")
        self.assertEqual(f"{self.profile.first_name}", "Maxx")
        self.assertEqual(f"{self.profile.middle_name}", "King")
        self.assertEqual(f"{self.profile.nickname}", "Bk")
        self.assertEqual(f"{self.profile.other_name}", "Bkay")
        self.assertEqual(f"{self.profile.sex}", "Male")
        self.assertEqual(f"{self.profile.other_gender}", "Male")
        self.assertEqual(f"{self.profile.date_of_birth}", "1996-03-06")


    def test_profile_list_view(self):
        response = self.client.get(reverse("student_profile:profile"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Maxx")
        self.assertTemplateUsed(response, "student_profile_list.html")


    def test_contact_detail(self):
        self.assertEqual(f"{self.contact.related_field}", "Maxx")
        self.assertEqual(f"{self.contact.phone_option}", "Home")
        self.assertEqual(f"{self.contact.phone_number}", "123 456 789")


    def test_address(self):
        self.assertEqual(f"{self.address.related_field}", "Maxx")
        self.assertEqual(f"{self.address.address}", "home 123")
        self.assertEqual(f"{self.address.city}", "Pretoria")
        self.assertEqual(f"{self.address.postal_code}", "1234")
        self.assertEqual(f"{self.address.country}", "South Africa")


    def test_demographics(self):
        self.assertEqual(f"{self.demographics.user}", "studentuser")
        self.assertEqual(f"{self.demographics.religion}", "Christianity")
        self.assertEqual(f"{self.demographics.race}", "Black")
        self.assertEqual(f"{self.demographics.consent}", "True")


    def test_language(self):
        self.assertEqual(f"{self.language.related_field}", "Christianity")
        self.assertEqual(f"{self.language.language}", "English")
        self.assertEqual(f"{self.language.language_proficiency}", "Speak")


    def test_citizenship(self):
        self.assertEqual(f"{self.citizenship.related_field}", "Christianity")
        self.assertEqual(f"{self.citizenship.name}", "South African")


    def test_family(self):
        self.assertEqual(f"{self.family.user}", "studentuser")
        self.assertEqual(f"{self.family.relationship_status}", "Married")
        self.assertEqual(f"{self.family.living_situation}", "With both parents")
        self.assertEqual(f"{self.family.children}", "False")
        self.assertEqual(f"{self.family.number_of_children}", "3")


    def test_parent(self):
        self.assertEqual(f"{self.parent.related_parent}", "Married")
        self.assertEqual(f"{self.parent.parent_type}", "Mother")
        self.assertEqual(f"{self.parent.parent_status}", "True")
        self.assertEqual(f"{self.parent.parent_prefix}", "Mrs.")
        self.assertEqual(f"{self.parent.first_name}", "Mary")
        self.assertEqual(f"{self.parent.middle_name}", "Samantha")
        self.assertEqual(f"{self.parent.last_name}", "Jones")
        self.assertEqual(f"{self.parent.birth_country}", "South Africa")
        self.assertEqual(f"{self.parent.preferred_email}", "testmom@email.com")
        self.assertEqual(f"{self.parent.phone_number}", "123 456 789")
        self.assertEqual(f"{self.parent.parent_address}", "Home 123")
        self.assertEqual(f"{self.parent.occupation}", "Teacher")
        self.assertEqual(f"{self.parent.education_level}", "College")


    def test_sibling(self):

        self.assertEqual(f"{self.sibling.related_parent}", "Married")
        self.assertEqual(f"{self.sibling.first_name}", "Philip")
        self.assertEqual(f"{self.sibling.middle_name}", "Sinothi")
        self.assertEqual(f"{self.sibling.last_name}", "Moyo")
        self.assertEqual(f"{self.sibling.date_of_birth}", "1990-08-20")
        self.assertEqual(f"{self.sibling.relationship}", "Brother")
        self.assertEqual(f"{self.sibling.education_level}", "University")


    def test_education(self):
        self.assertEqual(f"{self.education.user}", "studentuser")
        self.assertEqual(f"{self.education.school_name}", "Premier")
        self.assertEqual(f"{self.education.date_of_entry}", "2020-01-01")
        self.assertEqual(f"{self.education.school_type}", "True")
        self.assertEqual(f"{self.education.graduation_status}", "True")
        self.assertEqual(f"{self.education.graduation_date}", "2021-01-01")
        self.assertEqual(f"{self.education.progression_status}", "Graduate")
        self.assertEqual(f"{self.education.description}", "This text has to be here")


    def test_school_(self):
        self.assertEqual(f"{self.school.related_school}", "Premier")
        self.assertEqual(f"{self.school.school_name}", "Green Gables")
        self.assertEqual(f"{self.school.date_started}", "2020-01-01")
        self.assertEqual(f"{self.school.date_finished}", "2021-01-01")
        self.assertEqual(f"{self.school.description}", "This text has to be here")


    def test_future_plan(self):
        self.assertEqual(f"{self.futureplan.related_school}", "Premier")
        self.assertEqual(f"{self.futureplan.career_interest}", "Coding")
        self.assertEqual(f"{self.futureplan.highest_degree}", "Masters")
        self.assertEqual(f"{self.futureplan.notes}", "This text has to be here")
        

    def test_activity_check(self):
        self.assertEqual(f"{self.activitycheck.user}", "studentuser")
        self.assertEqual(f"{self.activitycheck.activity_interest}", "True")

    def test_activity(self):
        self.assertEqual(f"{self.activity.related_field}", "True")
        self.assertEqual(f"{self.activity.activity_type}", "Art")
        self.assertEqual(f"{self.activity.position}", "Leader")
        self.assertEqual(f"{self.activity.organization}", "WHO")
        self.assertEqual(f"{self.activity.accomplishment}", "Winner 2020")
        self.assertEqual(f"{self.activity.intension}", "True")
        self.assertEqual(f"{self.activity.hours_per_week}", "30")
        self.assertEqual(f"{self.activity.weeks_per_year}", "20")
        self.assertEqual(f"{self.activity.participation_time}", "2hrs")

    def test_personal_essay(self):
        self.assertEqual(f"{self.personalessay.user}", "studentuser")
        self.assertEqual(f"{self.personalessay.consent}", "True")
        self.assertEqual(f"{self.personalessay.essay}", "This text is supposed to be here")

    def test_disciplinary_history(self):
        self.assertEqual(f"{self.discipline.related_field}", "True")
        self.assertEqual(f"{self.discipline.disciplinary}", "Yes")

    def test_additional_information(self):
        self.assertEqual(f"{self.additionalinformation.related_field}", "True")
        self.assertEqual(f"{self.additionalinformation.any_disruptions}", "True")
        self.assertEqual(f"{self.additionalinformation.disruption}", "This text can be here")
        self.assertEqual(f"{self.additionalinformation.any_curcumstance}", "True")
        self.assertEqual(f"{self.additionalinformation.circumstance}", "This text can be here")

