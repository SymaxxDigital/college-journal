from django.forms.models import inlineformset_factory
from . models import *
from django import forms


class ActivityForm(forms.ModelForm):
   class Meta:
        model = Activity
        fields = "__all__" #("activity_interest", "activity_type", "position", "organization", "accomplishment", "intension", "hours_per_week", "weeks_per_year", "participation_time",)




"""Personal Information"""

ContactDetailFormSet = inlineformset_factory(PersonalInformation, ContactDetail, fields=[
                                             'related_field', 'phone_option', 'phone_number'], exclude=[], extra=1, can_delete=True)
AddressFormSet = inlineformset_factory(PersonalInformation, Address, fields=[
                                       'address', 'city', 'postal_code', 'country'], exclude=[], extra=1, can_delete=True)

"""Demographics"""

LanguageFormSet = inlineformset_factory(Demographic, Language, fields=[
                                        'related_field', 'language', 'language_proficiency'], exclude=[], extra=1, can_delete=True)
CitizenshipFormSet = inlineformset_factory(Demographic, Citizenship, fields=[
                                           'related_field', 'name'], exclude=[], extra=1, can_delete=True)

"""Family"""

ParentFormSet = inlineformset_factory(Family, Parent, fields=['related_parent', 'parent_type', 'parent_status', 'parent_prefix', 'first_name', 'middle_name', 'last_name',
                                      'birth_country', 'preferred_email', 'preferred_phone', 'phone_number', 'parent_address', 'occupation', 'education_level'], exclude=[], extra=1, can_delete=True)
SiblingFormSet = inlineformset_factory(Family, Sibling, fields=[
                                       'related_parent', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'relationship', 'education_level', ], exclude=[], extra=1, can_delete=True)


"""Education"""

SchoolFormSet = inlineformset_factory(Education, School, fields=[
                                      "related_school", "school_name", "date_started", "date_finished", "description"], exclude=[], extra=1, can_delete=True)
FuturePlanFormSet = inlineformset_factory(Education, FuturePlan, fields=[
                                          "related_school", "career_interest", "highest_degree", "notes"], exclude=[], extra=1, can_delete=True)

EducationFormSet = inlineformset_factory(Education, Activity, fields=["education", "activity_interest", "activity_type", "position", "organization", "accomplishment", "intension", "hours_per_week", "weeks_per_year", "participation_time"], exclude=[], extra=1, can_delete=True)


"""Activity"""

ActivityFormset = forms.formset_factory(ActivityForm, extra=1, can_delete=False)

"""Writing"""

DisciplinaryHistoryFormSet = inlineformset_factory(PersonalEssay, DisciplinaryHistory,  fields=[
                                                   "related_field", "disciplinary"], extra=1, can_delete=False)
AdditionalInformationFormSet = inlineformset_factory(PersonalEssay, AdditionalInformation, fields=[
                                                     "related_field", "any_disruptions", "disruption", "any_curcumstance", "circumstance"], exclude=[], extra=1, can_delete=True)
