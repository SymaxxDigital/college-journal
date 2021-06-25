from .models import PersonalInformation, Demographic, Family, Education, PersonalEssay
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import (
    ContactDetailFormSet, 
    AddressFormSet, 
    LanguageFormSet, 
    CitizenshipFormSet, 
    ParentFormSet, 
    SiblingFormSet,
    SchoolFormSet,
    FuturePlanFormSet,
    DisciplinaryHistoryFormSet,
    AdditionalInformationFormSet,
    EducationFormSet,
)


class ProfileView(ListView):
    """This will list all the available profiles"""
    model = PersonalInformation
    template_name = 'profile/student_profile_list.html'
    context_object_name = 'profiles'


class ProfileCreateView(CreateView):
    """This will be used to create the profiles for first time users"""
    model = PersonalInformation
    template_name = "profile/student_profile_create.html"
    success_url = reverse_lazy('student_profile:profile')
    fields = "__all__"


    def get_context_data(self, **kwargs):
        context = super(ProfileCreateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context["contact_formset"] = ContactDetailFormSet(self.request.POST)
            context["address_formset"] = AddressFormSet(self.request.POST)
        else:
            context["contact_formset"] = ContactDetailFormSet()
            context["address_formset"] = AddressFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset1 = context["contact_formset"]
        formset2 = context["address_formset"]

        if formset1.is_valid() and formset2.is_valid():
            response = super().form_valid(form)
            formset1.instance = self.object
            formset2.instance = self.object
            formset1.save()
            formset2.save()
            return response
        else:
            return super.form_valid(form)


class ProfileUpdateView(UpdateView):
    """This will be used to update or edit users information"""
    model = PersonalInformation
    template_name = "profile/student_profile_update.html"
    success_url = reverse_lazy('student_profile:profile')
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context["contact_formset"] = ContactDetailFormSet(self.request.POST, instance=self.object)
            context["address_formset"] = AddressFormSet(self.request.POST, instance=self.object)
        else:
            context["contact_formset"] = ContactDetailFormSet(instance=self.object)
            context["address_formset"] = AddressFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset1 = context["contact_formset"]
        formset2 = context["address_formset"]

        if formset1.is_valid() and formset2.is_valid():
            response = super().form_valid(form)
            formset1.instance = self.object
            formset2.instance = self.object
            formset1.save()
            formset2.save()
            return response
        else:
            return super.form_valid(form)


class DemographicListView(ListView):
    model = Demographic
    template_name = "profile/demographic_list.html"
    context_object_name = "demographics"


class DemographicCreateView(CreateView):
    """This will be used to create student demographics"""
    model = Demographic
    template_name = "profile/demographic_create.html"
    success_url = reverse_lazy("student_profile:profile")
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(DemographicCreateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context["language_formset"] = LanguageFormSet(self.request.POST)
            context["citizenship_formset"] = CitizenshipFormSet(self.request.POST)
        else:
            context["language_formset"] = LanguageFormSet()
            context["citizenship_formset"] = CitizenshipFormSet()
        return context


    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset1 = context["language_formset"]
        formset2 = context["citizenship_formset"]

        if formset1.is_valid() and formset2.is_valid():
            response = super().form_valid(form)
            formset1.instance = self.object
            formset2.instance = self.object
            formset1.save()
            formset2.save()
            return response
        else:
            return super.form_valid(form)


class DemographicUpdateView(UpdateView):

    """This will be used to create student demographics"""
    model = Demographic
    template_name = "profile/demographic_update.html"
    success_url = reverse_lazy("student_profile:profile")
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(DemographicUpdateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context["language_formset"] = LanguageFormSet(self.request.POST, instance=self.object)
            context["citizenship_formset"] = CitizenshipFormSet(self.request.POST, instance=self.object)
        else:
            context["language_formset"] = LanguageFormSet(instance=self.object)
            context["citizenship_formset"] = CitizenshipFormSet(instance=self.object)
        return context


    def form_valid(self, form):

        context = self.get_context_data(form=form)
        formset1 = context["language_formset"]
        formset2 = context["citizenship_formset"]

        if formset1.is_valid() and formset2.is_valid():
            response = super().form_valid(form)
            formset1.instance = self.object
            formset2.instance = self.object
            formset1.save()
            formset2.save()
            return response
        else:

            return super.form_valid(form)


class FamilyListView(ListView):
    model = Family
    template_name = "profile/family_list.html"
    context_object_name = "families"


class FamilyCreateView(CreateView):
    """This will create the family of the student"""
    model = Family
    template_name = "profile/family_create_view.html"
    success_url = reverse_lazy("student_profile:profile")
    fields = "__all__"


    def get_context_data(self, **kwargs):
        context = super(FamilyCreateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context["parent_formset"] = ParentFormSet(self.request.POST)
            context["sibling_formset"] = SiblingFormSet(self.request.POST)
        else:
            context["parent_formset"] = ParentFormSet()
            context["sibling_formset"] = SiblingFormSet()
        return context


    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset1 = context["parent_formset"]
        formset2 = context["sibling_formset"]

        if formset1.is_valid() and formset2.is_valid():
            response = super().form_valid(form)
            formset1.instance = self.object
            formset2.instance = self.object
            formset1.save()
            formset2.save()
            return response
        else:
            return super.form_valid(form)


class FamilyUpdateView(UpdateView):
    """This will create the family of the student"""
    model = Family
    template_name = "profile/family_update_view.html"
    success_url = reverse_lazy("student_profile:profile")
    fields = "__all__"


    def get_context_data(self, **kwargs):
        context = super(FamilyUpdateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context["parent_formset"] = ParentFormSet(self.request.POST, instance=self.object)
            context["sibling_formset"] = SiblingFormSet(self.request.POST, instance=self.object)
        else:
            context["parent_formset"] = ParentFormSet(instance=self.object)
            context["sibling_formset"] = SiblingFormSet(instance=self.object)
        return context


    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset1 = context["parent_formset"]
        formset2 = context["sibling_formset"]

        if formset1.is_valid() and formset2.is_valid():
            response = super().form_valid(form)
            formset1.instance = self.object
            formset2.instance = self.object
            formset1.save()
            formset2.save()
            return response
        else:
            return super.form_valid(form)


class EducationListView(ListView):
    model = Education
    template_name = "profile/education_list.html"
    context_object_name = "educations"


class EducationCreateView(CreateView):
    """This will create the Education profile of the student"""
    model = Education
    template_name = "profile/education_create_view.html"
    success_url = reverse_lazy("student_profile:profile")
    fields = "__all__"


    def get_context_data(self, **kwargs):
        context = super(EducationCreateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context["school_formset"] = SchoolFormSet(self.request.POST)
            context["futureplan_formset"] = FuturePlanFormSet(self.request.POST)
            context["activity_formset"] = FuturePlanFormSet(self.request.POST)
        else:
            context["school_formset"] = ParentFormSet()
            context["futureplan_formset"] = SiblingFormSet()
            context["activity_formset"] = EducationFormSet()

        return context


    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset1 = context["school_formset"]
        formset2 = context["futureplan_formset"]
        formset3 = context["EducationFormSet"]

        if formset1.is_valid() and formset2.is_valid() and formset3.is_valid():
            response = super().form_valid(form)
            formset1.instance = self.object
            formset2.instance = self.object
            formset3.instance = self.object
            formset1.save()
            formset2.save()
            formset3.save()
            return response
        else:
            return super.form_valid(form)


class EducationUpdateView(UpdateView):
    """This will create the family of the student"""
    model = Education
    template_name = "profile/education_update_view.html"
    success_url = reverse_lazy("student_profile:profile")
    fields = "__all__"


    def get_context_data(self, **kwargs):
        context = super(EducationUpdateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context["school_formset"] = SchoolFormSet(self.request.POST, instance=self.object)
            context["futureplan_formset"] = FuturePlanFormSet(self.request.POST, instance=self.object)
            context["activity_formset"] = FuturePlanFormSet(self.request.POST, instance=self.object)

        else:
            context["school_formset"] = SchoolFormSet(instance=self.object)
            context["futureplan_formset"] = FuturePlanFormSet(instance=self.object)
            context["activity_formset"] = EducationFormSet()

        return context


    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset1 = context["school_formset"]
        formset2 = context["futureplan_formset"]
        formset3 = context["activity_formset"]

        if formset1.is_valid() and formset2.is_valid() and formset3.is_valid():
            response = super().form_valid(form)
            formset1.instance = self.object
            formset2.instance = self.object
            formset3.instance = self.object
            formset1.save()
            formset2.save()
            formset3.save()
            return response
        else:
            return super.form_valid(form)


"""
class ActivityListView(ListView):
    model = Activity
    template_name = "profile/activity_list.html"
    context_object_name = "activities"


class ActivityCreateView(CreateView):
    This will create the Education profile of the student
    model = ActivityCheck
    template_name = "profile/activity_create.html"
    success_url = reverse_lazy("student_profile:profile")
    fields = "__all__"


    def get_context_data(self, **kwargs):
        context = super(ActivityCreateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context["activity_formset"] = ActivityFormSet(self.request.POST)
        else:
            context["activity_formset"] = ActivityFormSet()
        return context


    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context["activity_formset"]

        if formset.is_valid():
            response = super().form_valid(form)
            formset.instance = self.object
            formset.save()
            return response
        else:
            return super.form_valid(form)


class ActivityUpdateView(UpdateView):

    This will create the family of the student

    model = ActivityCheck
    template_name = "profile/activity_update.html"
    success_url = reverse_lazy("student_profile:profile")
    fields = "__all__"


    def get_context_data(self, **kwargs):
        context = super(ActivityUpdateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context["activity_formset"] = ActivityFormSet(self.request.POST, instance=self.object)
        else:
            context["activity_formset"] = ActivityFormSet(instance=self.object)
        return context


    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context["activity_formset"]

        if formset.is_valid():
            response = super().form_valid(form)
            formset.instance = self.object
            formset.save()
            return response
        else:
            return super.form_valid(form)

"""

class PersonalessayListView(ListView):
    model = PersonalEssay
    template_name = "profile/personal_essay_list.html"
    context_object_name = "personalessays"



class PersonalEssayCreateView(CreateView):
    """This will create the family of the student"""
    model = PersonalEssay
    template_name = "profile/personal_essay_create.html"
    success_url = reverse_lazy("student_profile:profile")
    fields = "__all__"


    def get_context_data(self, **kwargs):
        context = super(PersonalEssayCreateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context["dicipline_formset"] = DisciplinaryHistoryFormSet(self.request.POST)
            context["additional_formset"] = AdditionalInformationFormSet(self.request.POST)
        else:
            context["dicipline_formset"] = DisciplinaryHistoryFormSet()
            context["additional_formset"] = AdditionalInformationFormSet()
        return context


    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset1 = context["dicipline_formset"]
        formset2 = context["additional_formset"]

        if formset1.is_valid() and formset2.is_valid():
            response = super().form_valid(form)
            formset1.instance = self.object
            formset2.instance = self.object
            formset1.save()
            formset2.save()
            return response
        else:
            return super.form_valid(form)


class PersonalEssayUpdateView(UpdateView):
    """This will create the family of the student"""
    model = PersonalEssay
    template_name = "profile/personal_essay_update.html"
    success_url = reverse_lazy("student_profile:profile")
    fields = "__all__"


    def get_context_data(self, **kwargs):
        context = super(PersonalEssayUpdateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context["dicipline_formset"] = DisciplinaryHistoryFormSet(self.request.POST, instance=self.object)
            context["additional_formset"] = AdditionalInformationFormSet(self.request.POST, instance=self.object)
        else:
            context["dicipline_formset"] = DisciplinaryHistoryFormSet(instance=self.object)
            context["additional_formset"] = AdditionalInformationFormSet(instance=self.object)
        return context


    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset1 = context["dicipline_formset"]
        formset2 = context["additional_formset"]

        if formset1.is_valid() and formset2.is_valid():
            response = super().form_valid(form)
            formset1.instance = self.object
            formset2.instance = self.object
            formset1.save()
            formset2.save()
            return response
        else:
            return super.form_valid(form)
