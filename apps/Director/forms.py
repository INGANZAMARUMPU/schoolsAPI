from django import forms
from .models import *
from apps.Prefect.models import *
from apps.Base.models import *
from apps.Director.models import *
from apps.TeachersAndTitulars.models import *
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

# class CniForm(forms.ModelForm):
#
#     cni = forms.CharField(
#         widget = forms.TextInput(attrs = {'placeholder': 'Search CNI', 'class': 'form-control'}),
#         label = '')
#
#     class Meta:
#         model = Cni
#         fields = ('cni',)

class SearchUserForm(forms.ModelForm):

    search_user = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'Search username','aria-describedby':'basic-addon1', 'class': 'form-control'}),
        label = '')

    class Meta:
        model = SearchUser
        fields = ('search_user',)

class AddUsersForm(forms.Form):
    allusers_list = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        label='Excel file')

class AddUserForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Username ', 'class': 'form-control'}),
        label='Username')

    role = forms.ModelChoiceField(
        widget=forms.Select(attrs={'placeholder': ' ', 'class': 'form-control'}),
        queryset = Role.objects.all().exclude(url="director"),
        label='Role')

    # def clean_username(self, *args, **kwargs):
    #     username = self.cleaned_data.get("username")
    #     username1 = User.objects.filter(username = username)
    #     if str(username1) in username:
    #         return username1

class ProfilForm1(forms.ModelForm):

    user = forms.ModelChoiceField(
        widget=forms.Select(attrs={'placeholder': '', 'class': 'form-control'}),
        queryset = User.objects.all(),
        label='User')

    avatar = forms.ImageField(
        widget = forms.ClearableFileInput(attrs = {'placeholder': '', 'class': 'form-control'}),
        label='Avatar')

    class Meta:
        model = Profil
        fields = ('user', 'avatar',)

class CommuneForm(forms.ModelForm):

    name = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'Commune name', 'class': 'form-control'}),
        label = 'Commune')

    province = forms.ModelChoiceField(
        widget = forms.Select(attrs = {'placeholder': 'Province name', 'class': 'form-control'}),
        queryset = Province.objects.all(),
        label = 'Province')

    class Meta:
        model = Commune
        fields = ('name','province',)

class CourseForm(forms.ModelForm):

    name = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'Course Name', 'class': 'form-control'}),
        label='Course')

    c_lass = forms.ModelChoiceField(
        widget=forms.Select(attrs={'placeholder': 'Level', 'class': 'form-control'}),
        queryset=Class.objects.all(),
        label='Class')

    prof = forms.ModelChoiceField(
        widget=forms.Select(attrs={'placeholder': 'Level', 'class': 'form-control'}),
        queryset=Profil.objects.all(),
        label='Professor')

    max_ponderation = forms.IntegerField(
        widget = forms.NumberInput(attrs = {'placeholder': 'Level', 'class': 'form-control'}),
        label = 'Total Max')

    class Meta:
        model = Course
        fields = ('name','c_lass','prof','max_ponderation',)

class ProvinceForm(forms.ModelForm):

    name = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'Province name ', 'class': 'form-control'}),
        label = 'Province')

    class Meta:
        model = Province
        fields = ('name',)

class SchoolTypeForm(forms.ModelForm):

    education = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'School type', 'class': 'form-control'}),
        label = 'Type')

    class Meta:
        model = SchoolType
        fields = ('education',)

class SchoolForm(forms.ModelForm):

    name = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'School name ', 'class': 'form-control'}),
        label = 'School')

    province = forms.ModelChoiceField(
        widget=forms.Select(attrs = {'placeholder': '', 'class': 'form-control'}),
        queryset = Province.objects.all(),
        label = 'Province')

    commune = forms.ModelChoiceField(
        widget=forms.Select(attrs = {'placeholder': '', 'class': 'form-control'}),
        queryset = Commune.objects.all(),
        label = 'Commune')

    zone = forms.ModelChoiceField(
        widget=forms.Select(attrs = {'placeholder': '', 'class': 'form-control'}),
        queryset = Zone.objects.all(),
        label = 'Zone')

    school_type = forms.ModelChoiceField(
        widget=forms.Select(attrs = {'placeholder': '', 'class': 'form-control'}),
        queryset = SchoolType.objects.all(),
        label = 'School Type')

    description = forms.CharField(
        widget = forms.Textarea(attrs = {'placeholder': 'Description', 'class': 'form-control','rows':10,}),
        label = 'Description')

    class Meta:
        model = School
        fields = ('name','province','commune','zone','school_type','description',)

class ZoneForm(forms.ModelForm):

    name = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'Zone name', 'class': 'form-control'}),
        label = 'Zone')

    commune = forms.ModelChoiceField(
        widget = forms.Select(attrs = {'placeholder': 'Commune name', 'class': 'form-control'}),
        queryset = Commune.objects.all(),
        label = 'Commune')

    class Meta:
        model = Zone
        fields = ('name', 'commune', )
