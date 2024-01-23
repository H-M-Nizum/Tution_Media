from django.contrib import admin
from .models import TutionClassModel, TutionModel, ReviewModel, TeacherModel
# Register your models here.

# for slug fields. auto fillup slug fields in admin panale

class TutionClassAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(TutionClassModel, TutionClassAdmin)
admin.site.register(TutionModel)
admin.site.register(ReviewModel)
admin.site.register(TeacherModel)