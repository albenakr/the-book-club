from django.urls import path
from . import views

urlpatterns = [
    path('', views.plans, name='plans'),
    path('custom_plan/', views.custom_plans, name='custom_plans'),
    path('surprise_plans/', views.surprise_plans, name='surprise_plans'),
]
