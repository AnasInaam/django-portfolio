from django.contrib import admin
from .models import Skill, Project, Experience, Education, Contact, Profile


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency']
    list_filter = ['category']
    search_fields = ['name']
    ordering = ['category', '-proficiency']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'created_date']
    list_filter = ['featured', 'technologies', 'created_date']
    search_fields = ['title', 'description']
    filter_horizontal = ['technologies']
    ordering = ['-featured', '-created_date']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'start_date', 'end_date', 'is_current']
    list_filter = ['start_date', 'end_date']
    search_fields = ['company', 'position']
    ordering = ['-start_date']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date', 'end_date']
    list_filter = ['start_date', 'end_date']
    search_fields = ['institution', 'degree', 'field_of_study']
    ordering = ['-start_date']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_date', 'is_read']
    list_filter = ['is_read', 'created_date']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['created_date']
    ordering = ['-created_date']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email']
    search_fields = ['name', 'title']
    
    def has_add_permission(self, request):
        # Only allow one profile instance
        return not Profile.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Don't allow deletion of profile
        return False
