from .models import PersonalInformation, Demographic
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import ContactDetailFormSet, AddressFormSet, LanguageFormSet, CitizenshipFormSet


class ProfileView(ListView):
    """This will list all the available profiles"""
    model = PersonalInformation
    template_name = 'student_profile_list.html'
    context_object_name = 'profiles'


class ProfileCreateView(CreateView):
    """This will be used to create the profiles for first time users"""
    model = PersonalInformation
    template_name = "profile/student_profile_create.html"
    success_url = reverse_lazy('student_profile:profile')
    fields = "__all__"
    #fields = ("first_name", "middle_name", "last_name", "nickname", "other_name", "sex", "other_gender", "date_of_birth", )


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