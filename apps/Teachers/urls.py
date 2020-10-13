from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('teacher/<school>/', views.teacher_pannel_view, name="teacher"),
	path("teacher/course/<slug>/", views.course_view, name="course_view"),
	path("teacher/compile/<classe_id>/", views.compile_view, name="compile"),
	path("teacher/work/<slug>/<id>/", views.work_view, name="work_view"),
	path("teacher/edit/work/<id>", views.edit_work, name='edit_work'),
	path('teacher/delete/work/<id>/', views.delete_work_view, name="delete_work"),
	path('teacher/add_work/<slug>', views.add_work_view, name="add_work"),
	path('teacher/add_work/', views.add_work_view, name="add_work"),
	path('teacher/random_add_mark/<work_id>/', views.student_number_view, name="student_number"),
	path('teacher/random_add_mark/<work_id>/<pk>/', views.random_add_mark_view, name="random_add_mark"),
	path("teacher/load/<id>/", views.load_mark, name="load_mark"),
	path('teacher/work/edit_mark/<student_id>/<id>/', views.modify_mark_view, name="modify_mark"),
	path('teacher/add_mark/<work_id>/<int:page>/', views.add_mark_view, name="add_mark"),
	path('titular/<school>/', views.titular_pannel_view, name="titular"),
	path("titular/", views.titular_class_view, name="class_view"),
	path("titular/<slug>", views.titular_course_view, name="class_course_view"),

    
]

