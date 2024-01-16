from django import forms
from .models import TutionModel, ReviewModel

class TutionForm(forms.ModelForm):
    class Meta:
        model = TutionModel
        fields = ['tutionclass', 'subject', 'weekly_day', 'daily_time', 'location', 'fee']

class EditTutionForm(forms.ModelForm):
    class Meta:
        model = TutionModel
        fields = '__all__'

class ReviewForm(forms.ModelForm):
       
    class Meta:
        model = ReviewModel
        fields = ['body', 'ratting']
        
       