from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_treatments, name='treatments'),
    path('add/', views.add_treatment, name='add_treatment'),
    path('edit/<int:treatment_id>/', views.edit_treatment, name='edit_treatment'),
    path('delete/<int:treatment_id>/', views.delete_treatment, name='delete_treatment'),
]