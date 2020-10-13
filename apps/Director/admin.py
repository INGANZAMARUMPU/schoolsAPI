from django.contrib import admin
from .models import *
# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
	list_display = ('name', 'added_by', 'province', 'commune', \
		'zone', 'school_type', 'description', 'visible')
	list_filter = ('name', 'province', 'commune', 'zone')
	search_fields = ('name', 'province', 'commune', 'zone')
	prepopulated_fields = {'slug': ('name', )}

class SchoolTypeAdmin(admin.ModelAdmin):
	list_display = ('education',)
	list_filter = ('education',)
	search_fields = ('education',)

class CniAdmin(admin.ModelAdmin):
	list_display = ('cni',)
	list_filter = ('cni',)
	search_fields = ('cni',)

class ProvinceAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_filter = ('name',)
	search_fields = ('name',)
	prepopulated_fields = {'slug' : ('name', )}

class CommuneAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_filter = ('name',)
	search_fields = ('name',)
	prepopulated_fields = {'slug' : ('name', )}

class ZoneAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_filter = ('name',)
	search_fields = ('name',)
	prepopulated_fields = {'slug' : ('name', )}


admin.site.register(School, SchoolAdmin)
admin.site.register(SchoolType, SchoolTypeAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(Commune, CommuneAdmin)
admin.site.register(Zone, ZoneAdmin)
