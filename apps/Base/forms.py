from django import forms
from .models import *
from django.contrib.auth.models import User
from apps.Director.models import *


class ConnexionForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username ','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password ', 'type':'password','class':'form-control'}))

class InscriptionForm(forms.Form):
    firstname = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'First name ','class':'form-control'}), label='First name')
    lastname = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Last name ','class':'form-control'}), label='Last name')
    username = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Username ','class':'form-control'}), label='Username')
    password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Password ','class':'form-control'}), label='Password')
    password2 = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Confirm password ','class':'form-control'}), label='Confirm password')
    email = forms.EmailField( widget = forms.TextInput( attrs = {'placeholder':'Email address ','class':'form-control'} ), label='Email address')
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), label='Avatar')

class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Old password ','type':'password','class':'form-control col-xl-12 col-lg-12 col-12'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'New password ', 'type':'password','class':'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm password ', 'type':'password','class':'form-control'}))

class AttributionForm(forms.ModelForm):

    role = forms.ModelChoiceField(
        widget = forms.Select(attrs = {'placeholder': '', 'class': 'form-control'}),
        queryset = Role.objects.all().exclude(url="director"),
        label = 'Role')

    depuis = forms.DateTimeField(
        widget = forms.SelectDateWidget(attrs = {'placeholder': 'Date', 'class': 'form-control air-datepicker',}),
        label = 'From')

    class Meta:
        model = Attribution
        fields = ('role',)

class ProfilForm(forms.ModelForm):

    user = forms.ModelChoiceField(
        widget=forms.Select(attrs={'placeholder': '', 'class': 'form-control'}),
        queryset = User.objects.all(),
        label='User')

    avatar = forms.ImageField(
        widget = forms.ClearableFileInput(attrs = {'placeholder': '', 'class': 'form-control'}),
        label='Profil')

    about = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'About yourself', 'class': 'form-control'}),
        label='About')

    matricule = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'Matricule number', 'class': 'form-control'}),
        label='Matricule')

    birthday = forms.DateField(
        widget = forms.SelectDateWidget(attrs = {'placeholder': '', 'class': 'form-control'}),
        label='Date')

    father_name = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': '', 'class': 'form-control'}),
        label='Father name')

    mother_name = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': '', 'class': 'form-control'}),
        label='Mother name')

    CNI = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'Identity number', 'class': 'form-control'}),
        label='CNI')

    province = forms.ModelChoiceField(
        widget=forms.Select(attrs={'placeholder': '', 'class': 'form-control'}),
        queryset = Province.objects.all(),
        label='Province')

    commune = forms.ModelChoiceField(
        widget=forms.Select(attrs={'placeholder': '', 'class': 'form-control'}),
        queryset = Commune.objects.all(),
        label='Commune')

    zone = forms.ModelChoiceField(
        widget=forms.Select(attrs={'placeholder': '', 'class': 'form-control'}),
        queryset = Zone.objects.all(),
        label='Zone')

    CNI_recto = forms.ImageField(
        widget = forms.ClearableFileInput(attrs = {'placeholder': '', 'class': 'form-control'}),
        label='CNI Recto')

    CNI_verso = forms.ImageField(
        widget = forms.ClearableFileInput(attrs = {'placeholder': '', 'class': 'form-control'}),
        label='CNI Verso')


    class Meta:
        model = Profil
        fields = ('user', 'avatar', 'about', 'matricule', 'birthday', 'father_name', 'mother_name',
        'CNI_recto','CNI_verso', 'CNI', 'zone','commune','province',)

class RoleForm(forms.ModelForm):

    role = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'Role ', 'class': 'form-control'}),
        label = 'Role *')

    url = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'Url ', 'class': 'form-control'}),
        label = 'Url *')

    class Meta:
        model = Role
        fields = ('role','url',)
