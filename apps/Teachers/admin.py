from django.contrib import admin
from .models import *
# Register your models here.

class MarkAdmin(admin.ModelAdmin):
	list_display = ("student", "work", "marks")
	list_filter = ("student", "work", "marks")
	search_fields = ("student", "work", "marks")

class WorkAdmin(admin.ModelAdmin):
	list_display = ("course", "number", "school_year", "maxima", "date", "work_type", "is_valid")
	list_filter = ("course", "number", "school_year", "maxima", "date", "work_type", "is_valid")
	search_fields = ("course", "number", "school_year", "maxima", "date", "work_type", "is_valid")


class PresenceAdmin(admin.ModelAdmin):
	list_display = ("appel", "student", "is_present")
	list_filter = ("appel", "student", "is_present")
	search_fields = ("appel", "student", "is_present")

class AppelAdmin(admin.ModelAdmin):
	list_display = ("course", "date")
	list_filter = ("course", "date")
	search_fields = ("course", "date")





admin.site.register(Mark, MarkAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Presence, PresenceAdmin)
admin.site.register(Appel, AppelAdmin)
admin.site.register(Category)
admin.site.register(WorkType)
