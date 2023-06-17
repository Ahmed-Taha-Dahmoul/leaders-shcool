from django.urls import path
from . import views

app_name = 'a3ded'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home_page, name='home'),
    path('classes/', views.classes_view, name='classes'),
    path('classes/<int:class_id>/trimestre/', views.trimestre_view, name='trimestre'),  # Updated URL pattern
    path('classes/<int:class_id>/trimestre/<int:trimestre_id>/subjects/', views.subjects_view, name='subjects'),
    path('classes/<int:class_id>/trimestre/<int:trimestre_id>/subjects/<int:subject_id>/grades/', views.grades_view, name='grades'),
    # Add more URL patterns for other views as needed
]
