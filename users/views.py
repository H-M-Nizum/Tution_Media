from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import ApplicantModel
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.views.generic import FormView, DetailView, CreateView
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
# verify
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
# for email
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
# class UserRegistrationViews(FormView):
#     template_name = 'user_regostration.html'
#     form_class = forms.RegisterForm
#     success_url =reverse_lazy('login')
    
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return super().form_valid(form)




class RegistrationView(View):
    template_name = 'user_regostration.html'
    form_class = RegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save()

            # Generate token for email validation
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            # Build the activation link
            activation_link = reverse('activate', kwargs={'uidb64': uid, 'token': token})
            activation_link = request.build_absolute_uri(activation_link)

            # Send confirmation email
            email_subject = 'Confirm your email'
            email_body = render_to_string('confirm_email.html', {'activation_link': activation_link})

            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            return HttpResponse("Check your email for confirmation.")
        
        return render(request, self.template_name, {'form': form})


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = get_user_model().objects.get(pk=uid)

            if user and default_token_generator.check_token(user, token):
                user.is_active = True
                user.save()
                return HttpResponse("Your account is now activated. You can log in.")
            else:
                return HttpResponse("Activation link is invalid.")
        except Exception as e:
            return HttpResponse("Activation link is invalid.")




class Userloginviews(LoginView):
    template_name = 'user_login.html'
    
    def get_success_url(self):
        if self.request.user.is_active:
            return reverse_lazy('home')
        else:
            return reverse_lazy('register')
    
class userlogoutview(View):
    def get(self, request):
        logout(request)
        return redirect('home')


from apply_tution.models import ApplicationModel

@login_required
def profileview(request, username):
    applicant = get_object_or_404(ApplicantModel, user=request.user)
    
    selected_applications = ApplicationModel.objects.filter(applicant=applicant, appaly_status='Selected')
    user = get_object_or_404(User, username=username)
    
    applicant = get_object_or_404(ApplicantModel, user=user)
    print(applicant.mobile_no)
    return render(request, 'profile.html', {'data': applicant, 'application' : selected_applications})

