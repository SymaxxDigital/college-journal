from django.contrib import admin
from .models import (
    PersonalInformation, 
    ContactDetail,
    Address,
    Language,
    Demographic,
    Citizenship,
    Family,
    Parent,
    Sibling,
    Education,
    School,
    FuturePlan,
    ActivityCheck,
    Activity,
    DisciplinaryHistory,
    PersonalEssay,
    AdditionalInformation,
    
)



class ContactDetailInline(admin.StackedInline):
    model = ContactDetail
    extra = 1
    max_num = 3


class AddressInline(admin.StackedInline):
    model = Address
    extra = 0
    max_num = 2


class PersonalInformationAdmin(admin.ModelAdmin):
    inlines = [
        ContactDetailInline,
        AddressInline,
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


class CitizenshipInline(admin.StackedInline):
    model = Citizenship
    extra = 0
    max_num = 1


class DemographicsAdmin(admin.ModelAdmin):
    inlines = [
        CitizenshipInline,
        LanguageInline,
    ]


    list_display = ("religion", "race", "consent")

admin.site.register(Demographic, DemographicsAdmin)


class ParentInline(admin.StackedInline):
    model = Parent
    extra = 0
    max_num = 5


class SiblingInline(admin.StackedInline):
    model = Sibling
    extra = 0
    max_num = 10


class FamilyAdmin(admin.ModelAdmin):
    inlines = [
        ParentInline,
        SiblingInline,
    ]


    list_display = (
        "relationship_status", 
        "living_situation",
        "children",
        "number_of_children",
        
        )

admin.site.register(Family, FamilyAdmin)


class SchoolInline(admin.StackedInline):
    model = School
    extra = 0
    max_num = 5


class FuturePlanInline(admin.StackedInline):
    model = FuturePlan
    extra = 0
    max_num = 1


class EducationAdmin(admin.ModelAdmin):
    inlines = [
        SchoolInline,
        FuturePlanInline,

    ]

    list_display = (
        'school_name', 
        'date_of_entry', 
        'school_type', 
        'graduation_status', 
        'graduation_date', 
        'progression_status',
        'description',
    )

admin.site.register(Education, EducationAdmin)


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