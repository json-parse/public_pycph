from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job-offer/<int:pk>/', views.job_detail, name='job_detail'),
    path('job-offer/new', views.job_new, name='job_new'),
    path('job-draft/<int:pk>/', views.job_draft, name='job_draft'),
]
