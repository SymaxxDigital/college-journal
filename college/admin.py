from django.contrib import admin
from .models import College, ContactDetail, Address


class ContactDetailInline(admin.StackedInline):
    model = ContactDetail
    extra = 1
    max_num = 3


class AddressInline(admin.StackedInline):
    model = Address
    extra = 0
    max_num = 2


class CollegeAdmin(admin.ModelAdmin):
    inlines = [
        ContactDetailInline,
        AddressInline,
    ]

    list_display = (
        "name", 
        "date_established",
        
    )

admin.site.register(College, CollegeAdmin)
