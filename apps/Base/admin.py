from django.contrib import admin
from .models import *


class RoleAdmin(admin.ModelAdmin):
	list_display = ("role",)
	list_filter = ("role",)
	search_fields = ("role",)


class ProfilAdmin(admin.ModelAdmin):
	list_display = ("user", "avatar", "about", "matricule", "birthday", "father_name", "mother_name")
	list_filter = ("user", "avatar", "about", "matricule", "birthday", "father_name", "mother_name")
	search_fields = ("user", "avatar", "about", "matricule", "birthday", "father_name", "mother_name")

class AttributionAdmin(admin.ModelAdmin):
	list_display = ('user', 'role', 'school', 'depuis')
	list_filter = ('user', 'role', 'school', 'depuis')
	search_fields = ('user', 'role', 'school', 'depuis')

class SchoolYearAdmin(admin.ModelAdmin):
	list_display = ("start", "end" )
	list_filter = ("start", "end" )
	search_fields = ("start", "end" )



admin.site.register(Role, RoleAdmin)
admin.site.register(Profil, ProfilAdmin)
admin.site.register(Attribution, AttributionAdmin)
admin.site.register(SchoolYear, SchoolYearAdmin)



# Register your models here.
