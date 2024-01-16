from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models
from . import forms
from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.decorators import login_required
# Create your views here.

class AddTution(CreateView):
    model = models.TutionModel
    form_class = forms.TutionForm
    template_name = 'add_tution.html'

    success_url = reverse_lazy('add_tution')

@login_required
def seeTution(request, class_slug = None):
    data = models.TutionModel.objects.all()
    if class_slug is not None:
        tutionclass = models.TutionClassModel.objects.get(slug = class_slug)
        data = models.TutionModel.objects.filter(tutionclass = tutionclass)
        
    tutionclass = models.TutionClassModel.objects.all()
    return render(request, 'seeTution.html', {'data':data, 'tutionclass': tutionclass})

class EditTutionView(UpdateView):
    model = models.TutionModel
    form_class = forms.EditTutionForm
    template_name = 'edit_tution.html'
    success_url = reverse_lazy('seeTution') 

@user_passes_test(lambda u: u.is_superuser)
def delete_tution(request, id):
    record = models.TutionModel.objects.get(pk=id)
    record.delete()
    return redirect('seeTution')



@login_required
def review_view(request, tution_id):
    tution = get_object_or_404(models.TutionModel, pk=tution_id)
    
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user.applicantmodel
            review.tution = tution
            review.save()
            return redirect('seeTution')  
    else:
        form = forms.ReviewForm()

    return render(request, 'review.html', {'form': form, 'tution': tution})

from .models import TutionModel, ReviewModel
@login_required
def tution_reviews_view(request, tution_id):
    tution = get_object_or_404(TutionModel, pk=tution_id)
    reviews = ReviewModel.objects.filter(tution=tution)

    return render(request, 'display_review.html', {'tution': tution, 'reviews': reviews})
