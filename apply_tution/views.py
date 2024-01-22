# views.py
from django.shortcuts import get_object_or_404, redirect, render
from .models import ApplicationModel
from django.contrib.auth.decorators import login_required
from tution.models import TutionModel
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

@login_required
def apply_tution(request, tution_id):
    tution = get_object_or_404(TutionModel, pk=tution_id)
    applicant = request.user.applicantmodel

    # Check if the user has already applied to this tuition
    existing_application = ApplicationModel.objects.filter(applicant=applicant, tution=tution).first()

    if existing_application:
        messages.warning(
                request,
                f' You Already Apply this Tution!!!')

    else:
         messages.success(
                request,
                f' Congratulations . Successfully Apply for this tution.')

    # Create a new application
    ApplicationModel.objects.create(applicant=applicant, tution=tution)

    return redirect('seeTution')




@user_passes_test(lambda u: u.is_superuser)
def admin_all_applications_views(request, tution_id):
    tution = get_object_or_404(TutionModel, pk=tution_id)
    applications = ApplicationModel.objects.filter(tution=tution)
    return render(request, 'all_applications.html', {'applications': applications, 'tution': tution})


from django.template.loader import render_to_string
# for email
from django.core.mail import EmailMultiAlternatives

@user_passes_test(lambda u: u.is_superuser)
def confirm_application(request, application_id):
    application = get_object_or_404(ApplicationModel, pk=application_id)
        # Handle confirmation logic
    application.appaly_status = "Selected"
    application.save()

   # Send confirmation email
    email_subject = 'Confirm your email'
    email_body = render_to_string('selected_email.html', {'application' : application})

    email = EmailMultiAlternatives(email_subject, '', to=[application.applicant.user.email])
    email.attach_alternative(email_body, "text/html")
    email.send()

    return redirect('seeTution')

