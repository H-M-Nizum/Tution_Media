# urls.py
from django.urls import path
from .views import apply_tution, admin_all_applications_views, confirm_application

urlpatterns = [
    
    path('apply/<int:tution_id>/', apply_tution, name='apply_tution'),
    path('application/<int:tution_id>/', admin_all_applications_views, name='application'),
    path('confirm_application/<int:application_id>/', confirm_application, name='confirm_application'),

]
