from django.contrib import admin

from readthedocs.models import Project

class ProjectAdmin(admin.ModelAdmin):
    search_fields = ['description']
    list_filter = ['programming_language', 'documentation_type']

admin.site.register(Project, ProjectAdmin)
