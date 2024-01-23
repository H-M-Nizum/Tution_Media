from django.contrib import admin

from .models import ApplicantModel, ContactModel
# Register your models here.

admin.site.register(ApplicantModel)
admin.site.register(ContactModel)