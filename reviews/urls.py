from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('write_review/<book_id>/', views.write_review, name='write_review'),
    path('delete_review/<review_id>/', views.delete_review, name='delete_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
