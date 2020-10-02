from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.plans, name='plans'),
    path('custom_plan/', views.custom_plans, name='custom_plans'),
    path('view_custom_plan_details/<plan_id>', views.view_custom_plan_details, name='view_custom_plan_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
