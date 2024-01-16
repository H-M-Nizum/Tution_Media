from django.db import models
from users.models import ApplicantModel
from tution.models import TutionModel
# Create your models here.
APPALY_STATUS = [
    ('Pending', 'Pending'),
    ('Selected', 'Selected'),
    ('Completed', 'Completed'),
]
class ApplicationModel(models.Model):
    applicant = models.ForeignKey(ApplicantModel, on_delete=models.CASCADE)
    tution = models.ForeignKey(TutionModel, on_delete=models.CASCADE)
    appaly_status = models.CharField(max_length=30, choices=APPALY_STATUS, default='Pending')
    created_time = models.DateTimeField(auto_now_add=True)
    cancel = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.applicant.user.first_name} to {self.tution.subject}"


