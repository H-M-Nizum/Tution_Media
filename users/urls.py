

from django.urls import path

from . import views

urlpatterns = [
    path('register/',  views.RegistrationView.as_view(), name='register'),
    path('activate/<uidb64>/<token>/', views.ActivateAccountView.as_view(), name='activate'),
    path('contact/', views.Contactview.as_view(), name='contact'),

    path('login/',  views.Userloginviews.as_view(), name='login'),
    path('profile/<str:username>/',  views.profileview, name='profile'),
    path('history/<str:username>/',  views.Tutionhistory, name='history'),
    path('logout/',  views.userlogoutview.as_view(), name='logout'),

    path('pass_change/', views.password_change, name='pass_change'),

]