from django.db import models
from django.contrib.auth.models import User
from users.models import ApplicantModel
# Create your models here.


class TutionClassModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

TUTION_STATUS = [
    ('Running', 'Running'),
    ('Completed', 'Completed'),
]

class TutionModel(models.Model):
    tutionclass = models.ManyToManyField(TutionClassModel)
    subject = models.CharField(max_length=100)
    weekly_day = models.IntegerField()
    daily_time = models.IntegerField()
    location = models.CharField(max_length=200)
    fee = models.IntegerField()
    tution_status = models.CharField(max_length=30, choices=TUTION_STATUS, default='Running')

STAR_CHOICE = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class ReviewModel(models.Model):
    reviewer = models.ForeignKey(ApplicantModel, on_delete=models.CASCADE)
    tution = models.ForeignKey(TutionModel, on_delete=models.CASCADE)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    ratting = models.CharField(max_length=100, choices = STAR_CHOICE)


    def __str__(self):
        return f"{self.reviewer.user.first_name} to {self.tution.subject}"
    

class TeacherModel(models.Model):
    image = models.ImageField(upload_to='tution/images/', blank = True,null = True)
    code = models.IntegerField()
    fullname = models.CharField(max_length=100)
    university = models.CharField(max_length=150)
    sub = models.CharField(max_length=150)
    ex_location = models.CharField(max_length=150)
    ex_class= models.CharField(max_length=150)
    living_place = models.CharField(max_length=150)
    ex_salary = models.IntegerField()

    def __str__(self):
        return self.fullname
    