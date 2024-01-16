from django.contrib import admin
from .models import ApplicationModel
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant_name', 'tution_id', 'appaly_status', 'created_time', 'cancel']

    def applicant_name(self, obj):
        return obj.applicant.user.first_name

    def tution_id(self, obj):
        return obj.tution.id


admin.site.register(ApplicationModel, ApplicationAdmin)