from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

   path('dir/hpanel/', views.home_view, name="hpanel"),
   path('<school>/', views.index, name="home"),
   path('<school>/', views.index, name="director"),
   path('attribute/<int:id>/<str:slug>/', views.attribute_view, name="attribute"),
   path('role/', views.role_view, name="role"),
   path('choose_user/<school>/', views.choose_user_view, name="choose_user"),
   path('add_user/<school>/', views.add_user_view, name="add_user"),
   path('add_users/<school>/<int:roley>/', views.add_users_list, name="add_users"),
   path('school_details/<str:slug>/', views.school_details_view, name="school_details"),
   path('view_employee/<str:slug>/', views.view_employee_view, name="view_employee"),
 


# paths for adding
   path('dir/add_province/', views.add_province_view, name="add_province"),
   path('dir/add_commune/', views.add_commune_view, name="add_commune"),
   path('dir/add_zone/', views.add_zone_view, name="add_zone"),
   path('dir/add_school/', views.add_school_view, name="add_school"),
   path('dir/add_schooltype/', views.add_schooltype_view, name="add_schooltype"),
   path('dir/add_role/', views.role_view, name="add_role"),

# paths for deletions
   path('delete_province/<str:slug>/', views.delete_province_view, name="delete_province"),
   path('delete_commune/<str:slug>/', views.delete_commune_view, name="delete_commune"),
   path('delete_zone/<str:slug>/', views.delete_zone_view, name="delete_zone"),
   path('delete_school/<str:slug>/', views.delete_school_view, name="delete_school"),
   path('delete_schooltype/<int:id>/', views.delete_schooltype_view, name="delete_schooltype"),
   path('delete_role/<int:id>/', views.delete_role_view, name="delete_role"),
   path('delete_attribution/<int:id>/<str:slug>/', views.delete_attribution_view, name="delete_attribution"),


# paths for updating
   path('update_province/<int:id>/', views.update_province_view, name="update_province"),
   path('update_commune/<int:id>/', views.update_commune_view, name="update_commune"),
   path('update_zone/<int:id>/', views.update_zone_view, name="update_zone"),
   path('update_school/<int:id>/', views.update_school_view, name="update_school"),
   path('update_schooltype/<int:id>/', views.update_schooltype_view, name="update_schooltype"),
   path('update_role/<int:id>/', views.update_role_view, name="update_role"),
   path('update_attribution/<int:id>/<str:slug>/', views.update_attribution_view, name="update_attribution"),

]
