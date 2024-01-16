from django.urls import path
from . import views

urlpatterns = [
    
    path('add/', views.AddTution.as_view(), name='add_tution'),
    path('seeTution/',  views.seeTution, name='seeTution'),
    path('class/<slug:class_slug>/', views.seeTution, name='class_slug'),
    path('edit/<int:pk>/', views.EditTutionView.as_view(), name='edit_tution'),
    path('delete/<int:id>/', views.delete_tution, name='delete_tution'),
    path('review/<int:tution_id>/', views.review_view, name='review'),
    path('reviews/<int:tution_id>/', views.tution_reviews_view, name='tution_reviews'),


    
]


