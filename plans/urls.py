from django.urls import path
from . import views

urlpatterns = [
    path('', views.plans, name='plans'),
    path('custom_plan/', views.custom_plans, name='custom_plans'),
    path('view_custom_plan_details/<plan_id>', views.view_custom_plan_details, name='view_custom_plan_details'),
]
