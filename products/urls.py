from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.all_books, name='books'),
    path('<book_id>', views.book_detail, name='book_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
