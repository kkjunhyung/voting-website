from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('vote/<int:project_id>/', views.vote, name='vote'),
]