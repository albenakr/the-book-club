from django.contrib import admin
from .models import Review


# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'book',
        'rating',
        'user_profile',
        'date',
        'title',
        'review_text',
    )


admin.site.register(Review, ReviewAdmin)
