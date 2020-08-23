from django.contrib import admin
from .models import Book, Genre, Language

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'publication_year',
        'price',
        'genre',
        'language',
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
admin.site.register(Language)

