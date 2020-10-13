from django.contrib.auth.models import User
from django import forms
from .models import *
from apps.Base.models import *
from apps.Prefect.models import *

class MarkForm(forms.ModelForm):
    marks = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': ' ', 'class': 'form-control'}),
        label='marks')
    
    class Meta:
        model = Mark
        fields = ('marks',)

    

class WorkForm(forms.ModelForm):

	# number = forms.IntegerField(
	# 	widget = forms.NumberInput(attrs={'placeholder' : '', 'class' : 'form-control'}), label='number')
	school_year = forms.ModelChoiceField(
		widget=forms.Select(attrs = {'placeholder' : '', 'class' : 'form-control'}),
		queryset = SchoolYear.objects.all(),
		label='SchoolYear')
	maxima = forms.IntegerField(
		widget = forms.NumberInput(attrs = {'placeholder' : '', 'class' : 'form-control'}),
		label='maxima')
	date = forms.DateField(
		widget = forms.SelectDateWidget(attrs = {'placeholder' : '', 'class' : 'form-control'}),
		label='date')
	
	class Meta:
		model = Work
		fields = ('school_year', 'date', 'maxima', 'is_valid' ,'work_type', 'category')


class LoadMarkForm(forms.Form):
    fichier = forms.FileField(
        widget = forms.ClearableFileInput(attrs = {'placeholder': 'students List', 'class': 'form-control'}),
        label = 'Select the mark excel File')


class StudentNumberForm(forms.Form):
	student_number = forms.IntegerField(
		widget= forms.NumberInput(attrs = {'placeholder' : 'N°', 'class' : 'form-control'}),
		label='Student number')

class StudentMarkForm(forms.Form):
	student_marks = forms.IntegerField(
		widget = forms.NumberInput(attrs = {'placeholder' : 'marks', 'class' : 'form-control'}),
		label='Student marks')