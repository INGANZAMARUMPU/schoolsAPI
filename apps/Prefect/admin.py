from django.contrib import admin
from .models import *
# Register your models here.
class ClassAdmin(admin.ModelAdmin):
	list_display = ("section", "school", "level", )
	list_filter = ("section", "school", "level", )
	search_fields = ("section", "school", "level", )

class CourseAdmin(admin.ModelAdmin):
	list_display = ('name', 'Class', 'prof', 'max_ponderation')
	list_filter = ('name', 'Class', 'prof', 'max_ponderation')
	search_fields = ('name', 'Class', 'prof', 'max_ponderation')
	prepopulated_fields = {'slug': ('name', 'Class')}

class LevelAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_filter = ('name',)
	search_fields = ('name',)

class SectionAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_filter = ('name',)
	search_fields = ('name',)

class StudentAdmin(admin.ModelAdmin):
	list_display = ('firstname', 'lastname', 'Class', 'admission_date')
	list_filter = ('firstname', 'lastname', 'Class', 'admission_date')
	search_fields = ('firstname', 'lastname', 'Class', 'admission_date')



admin.site.register(Class, ClassAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(StudentWork)