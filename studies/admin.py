# studies/admin.py
from django.contrib import admin
from .models import Study

class StudyAdmin(admin.ModelAdmin):
    list_display = ('study_name', 'study_phase', 'sponsor_name')  # Columns to display
    search_fields = ('study_name', 'sponsor_name')  # Fields searchable in the admin

admin.site.register(Study, StudyAdmin)
