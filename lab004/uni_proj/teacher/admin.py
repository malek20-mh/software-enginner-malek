from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'department', 'hire_date', 'is_active')
    search_fields = ('full_name', 'email', 'department')
    list_filter = ('department', 'is_active')
