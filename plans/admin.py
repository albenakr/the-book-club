from django.contrib import admin
from .models import Plan


# Register your models here.
class PlanAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'plan_duration',
        'price',
    )


admin.site.register(Plan, PlanAdmin)
