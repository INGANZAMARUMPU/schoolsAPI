from django import forms
from .models import *
from apps.Base.models import *
from django.contrib.auth.models import User

class LoadStudentsForm(forms.Form):
    list_student = forms.FileField(
        widget = forms.ClearableFileInput(attrs = {'placeholder': 'students List', 'class': 'form-control'}),
        label = 'Select the excel File')

class ClassForm(forms.ModelForm):

    section = forms.ModelChoiceField(
        widget = forms.Select(attrs = {'placeholder': 'Section name', 'class': 'form-control'}),
        queryset = Section.objects.all(),
        label = 'Section')

    level = forms.ModelChoiceField(
        widget = forms.Select(attrs = {'placeholder': 'Level', 'class': 'form-control'}),
        queryset = Level.objects.all(),
        label = 'Level')

    titulaire = forms.ModelChoiceField(
        widget = forms.Select(attrs = {'placeholder': 'Titular', 'class': 'form-control'}),
        queryset = None,
        label = 'Titular')

    group = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'Group', 'class': 'form-control'}),
        label = 'Group')

    class Meta:
        model = Class
        fields = ('level','group','section', 'titulaire')

    def __init__(self, *args, **kwargs):
        super(ClassForm, self).__init__(*args, **kwargs)
        self.base_fields["titulaire"].queryset = Profil.objects.all()

class CourseForm(forms.ModelForm):

    name = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'Course Name', 'class': 'form-control'}),
        label='Course')

    prof = forms.ModelChoiceField(
        widget=forms.Select(attrs={'placeholder': 'Level', 'class': 'form-control'}),
        queryset=None,
        label='Professor')

    max_ponderation = forms.IntegerField(
        widget = forms.NumberInput(attrs = {'placeholder': 'max ponderation', 'class': 'form-control'}),
        label = 'Total Max')

    duration = forms.IntegerField(
        widget = forms.NumberInput(attrs = {'placeholder': 'duration in hours', 'class': 'form-control'}),
        label = 'Duration')

    def __init__(self, profs, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.base_fields["prof"].queryset = profs

    class Meta:
        model = Course
        fields = ('name','prof','max_ponderation','duration')

class LevelForm(forms.ModelForm):

    name = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'Level', 'class': 'form-control'}),
        label = 'Level')

    class Meta:
        model = Level
        fields = ('name',)

class SectionForm(forms.ModelForm):

    name = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'Section Name', 'class': 'form-control'}),
        label = 'Section *')

    class Meta:
        model = Section
        fields = ('name',)

class StudentForm(forms.ModelForm):

    complete_identity = forms.ModelChoiceField(
        required=False,
        widget = forms.Select(attrs = {'placeholder': 'Titre ', 'class': 'form-control'}),
        queryset = Profil.objects.all(),
        label = 'Profil',)

    firstname = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'student\' firstname', 'class': 'form-control'}),
        label = 'firstname')

    lastname = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'student\' lastname', 'class': 'form-control'}),
        label = 'lastname')

    class Meta:
        model = Student
        fields = "__all__"
        exclude = ("Class", "admission_date")
