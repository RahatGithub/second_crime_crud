from django.contrib import admin
from .models import Investigator, Reporter

# Register your models here.
@admin.register(Reporter)
class ReporterAdmin(admin.ModelAdmin):
    list_display = ("reporter_code", "name", "phone", "email")


@admin.register(Investigator)
class InvestigatorAdmin(admin.ModelAdmin):
    list_display = ("investigator_code", "name", "phone", "email")