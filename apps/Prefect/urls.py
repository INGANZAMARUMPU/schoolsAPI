from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path("<school>", views.index, name="prefect"),
	path("<school>", views.index, name="discipline"),
	path("course/<slug>", views.course, name="prefect_course"),
	path("courses/<int:id_class>", views.courses, name="prefect_courses"),
	path("add_class/<school>/", views.addClass, name="add_class"),
	# path("add_level/<school>/", views.addLevel, name="add_level"),
	path("add_section/<school>/", views.addSection, name="add_section"),
	path("add_course/<classe_id>/", views.addCourse, name="add_course"),
	path("bulettin/<student_id>/<class_id>", views.bulettin, name="bulettin"),
	path("bulettins/<class_id>", views.bulettins, name="bulettins"),
	path("add_student/<classe>/", views.addStudent, name="add_student"),
	path("load_student/<classe>/", views.loadStudent, name="load_student"),
	path("edit_student/<student_id>/", views.editStudent, name="edit_student"),
	path("delete_student/<student_id>/", views.deleteStudent, name="delete_student"),
	path("modify_class/<class_id>/", views.modifyClass, name="modify_class"),
	path("modify_course/<slug>/", views.modifyCourse, name="modify_course"),
	path("delete_class/<class_id>/", views.deleteClass, name="delete_class"),
	path("delete_course/<slug>/", views.deleteCourse, name="delete_course"),
]
