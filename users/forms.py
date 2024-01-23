# django builtin model forom
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import ApplicantModel, ContactModel

class RegisterForm(UserCreationForm):
    
    # If i want to any fields custom modify
    mobile_no = forms.CharField(max_length=12)
    educational_qualification = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        
        fields = ['username', 'first_name', 'last_name', 'email', 'mobile_no', 'educational_qualification']
        
    def save(self, commit= True):
        user =  super().save(commit=False)
        if commit == True:
            user.is_active = False
            user.save() # user model a data save hobe
             
            print(self.cleaned_data['mobile_no'])
            # UserBankAccountModel model a data save hobe
            ApplicantModel.objects.create(
                user = user,
                mobile_no = self.cleaned_data['mobile_no'],
                educational_qualification = self.cleaned_data['educational_qualification']
            )
            
        return user


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
