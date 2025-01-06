from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_treatments, name='treatments'),
    path('add/', views.add_treatment, name='add_treatment'),
]