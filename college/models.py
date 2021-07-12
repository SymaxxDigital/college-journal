from django.db import models
from django.conf import settings


class College(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True, unique=True)
    date_established = models.DateField()

    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = "College"
        verbose_name_plural = "Colleges"


class ContactDetail(models.Model):
    """ Student contact details """

    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name="contacts", null=True, blank=True)
    phone_name = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.phone_option} {self.phone_name}"


class Address(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name="addresses", null=True, blank=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    

    def __str__(self):
        return f"{self.address} {self.city} {self.country}"
