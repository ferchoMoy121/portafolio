from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('experience/', views.experience, name='experience'),
    path('skills/', views.skills, name='skills'),
    path('certifications/', views.certifications, name='certifications'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('projects/<str:slug>/', views.project_detail, name='project_detail'),
]