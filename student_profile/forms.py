from django.forms.models import inlineformset_factory
from . models import *


"""Personal Information"""

ContactDetailFormSet = inlineformset_factory(PersonalInformation, ContactDetail, fields = ['related_field', 'phone_option', 'phone_number'], exclude = [], extra=1, can_delete = True)
AddressFormSet = inlineformset_factory(PersonalInformation, Address, fields = ['address', 'city', 'postal_code', 'country'], exclude = [], extra=1, can_delete = True)

"""Demographics"""

LanguageFormSet = inlineformset_factory(Demographic, Language, fields = ['related_field', 'language', 'language_proficiency'], exclude = [], extra=1, can_delete = True)
CitizenshipFormSet = inlineformset_factory(Demographic, Citizenship, fields = ['related_field', 'name'], exclude = [], extra=1, can_delete = True)