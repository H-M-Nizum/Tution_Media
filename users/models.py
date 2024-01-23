from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ApplicantModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=12)
    educational_qualification = models.TextField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class ContactModel(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.fullname
    