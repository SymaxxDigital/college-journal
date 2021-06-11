from django.contrib import admin
from .models import (
    PersonalInformation, 
    ContactDetail,
    Language,
    Demographic,
    Citizenship,
    Household,
    Parent,
    SecondParent,
    Sibling,
    Address,
    Address2,
    School,
    OtherSchool,
    SchoolDescription,
    FuturePlan,
    ActivityCheck,
    Activity,
    DisciplinaryHistory,
    PersonalEssay,
    AdditionalInformation,
)

admin.site.register(Household)
admin.site.register(FuturePlan)


class CitizenshipInline(admin.StackedInline):
    model = Citizenship
    extra = 0
    max_num = 1



class ContactDetailInline(admin.StackedInline):
    model = ContactDetail
    extra = 1
    max_num = 3


class PersonalInformationAdmin(admin.ModelAdmin):
    inlines = [
        ContactDetailInline,
    ]


    list_display = (
        "first_name", 
        "middle_name", 
        "last_name", 
        "nickname", 
        "other_name", 
        "sex", 
        "other_gender", 
        "date_of_birth"
    )

admin.site.register(PersonalInformation, PersonalInformationAdmin)


class LanguageInline(admin.StackedInline):
    model = Language
    extra = 1
    max_num = 5


class DemographicsAdmin(admin.ModelAdmin):
    inlines = [
        CitizenshipInline,
        LanguageInline,
    ]


    list_display = ("religion", "race", "consent")

admin.site.register(Demographic, DemographicsAdmin)


class AddressInline(admin.StackedInline):
    model = Address2
    extra = 0
    max_num = 1


class AddressAdmin(admin.ModelAdmin):
    inlines = [
        AddressInline,
    ]


    list_display = ('address', "postal_code", "city", "country",)

admin.site.register(Address, AddressAdmin)


class ParentInline(admin.StackedInline):
    model = SecondParent
    extra = 0
    max_num = 1


class SiblingInline(admin.StackedInline):
    model = Sibling
    extra = 0
    max_num = 1


class ParentAdmin(admin.ModelAdmin):
    inlines = [
        ParentInline,
        SiblingInline,
    ]


    list_display = (
        "parent_type", 
        "parent_status",
        "parent_prefix",
        "first_name",
        "middle_name",
        "last_name",
        "birth_country",
        "preferred_email",
        "preferred_phone",
        "phone_number",
        "parent_address",
        "occupation",
        "education_level",

        )

admin.site.register(Parent, ParentAdmin)


class SchoolInline(admin.StackedInline):
    model = OtherSchool
    extra = 0
    max_num = 5

class SchoolDescriptionInline(admin.StackedInline):
    model = SchoolDescription
    extra = 0
    max_num = 1


class SchoolAdmin(admin.ModelAdmin):
    inlines = [
        SchoolInline,
        SchoolDescriptionInline

    ]

    list_display = (
        'school_name', 
        'date_of_entry', 
        'school_type', 
        'graduation_status', 
        'graduation_date', 
        'progression_status'
    )

admin.site.register(School, SchoolAdmin)


class ActivityInline(admin.StackedInline):
    model = Activity
    extra = 1
    max_num = 6


class ActivityCheckAdmin(admin.ModelAdmin):
    inlines = [

        ActivityInline,
    ]

    list_display = (
        'activity_interest', 
       
    )

admin.site.register(ActivityCheck, ActivityCheckAdmin)


class DisciplinaryHistoryInline(admin.StackedInline):
    model = DisciplinaryHistory
    extra = 0
    max_num = 1

class AdditionalInformationInline(admin.StackedInline):
    model = AdditionalInformation
    extra = 0
    max_num = 1


class PersonalEssayAdmin(admin.ModelAdmin):
    inlines = [

        DisciplinaryHistoryInline,
        AdditionalInformationInline,
    ]

    list_display = (
        'consent', 
        'essay', 
       
    )

admin.site.register(PersonalEssay, PersonalEssayAdmin)