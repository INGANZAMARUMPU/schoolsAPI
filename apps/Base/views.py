from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .forms import *

# Create your views here.
def disconnect(request):
	show_hidden = "hidden"
	logout(request)
	return redirect(index)

def connect(request):
	show_hidden = "hidden"
	formulaire = ConnexionForm(request.POST)
	try:
		next_p = request.GET["next"]
	except:
		next_p = ""
	if request.method == "POST" and formulaire.is_valid():
		username = formulaire.cleaned_data['username']
		password = formulaire.cleaned_data['password']
		user = authenticate(username=username, password=password)
		print(username, password)
		if user:  # Si l'objet renvoyé n'est pas None
			login(request, user)
			messages.success(request, "You're now connected!")
			if next_p:
				return redirect(next_p)
			else:
				return redirect(index)
		# elif password.len() < 6:
		# 	messages.error(request, "Wrong password!")
		else:
			messages.error(request, "Wrong password!")
	formulaire = ConnexionForm()
	return render(request, 'sign-in.html', locals())

def inscription(request):
	show_hidden = "hidden"
	if request.method == "POST" :
		form = InscriptionForm(request.POST, request.FILES)
		if form.is_valid():
			username = form.cleaned_data['username']
			firstname = form.cleaned_data['firstname']
			lastname = form.cleaned_data['lastname']
			password = form.cleaned_data['password']
			password2 = form.cleaned_data['password2']
			email = form.cleaned_data['email']
			avatar = form.cleaned_data['avatar']
			if password==password2:
				user = User.objects.create_user(
					username=username,
					email=email,
					password=password)
				user.first_name, user.last_name = firstname, lastname
				user.save()
				print(username, email, firstname, lastname, password)
				Profil(user=user, avatar=avatar).save()
				messages.success(request, "Hello "+username+", youn are registered successfully!")
				if user:
					login(request, user)
					return redirect(index)
	form = InscriptionForm()
	return render(request, 'inscription.html', locals())

@login_required
def index(request):
	show_hidden = "hidden"
	h3 = "Dashboard"
	try:
		attributions = Attribution.objects.filter(user=request.user)
	except Exception as e:
		print("user has no profile")
	return render(request, "index.html", locals())

@login_required
def change_password(request):
	show_hidden = "hidden"
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Your password was successfully updated!')
			return redirect('home')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'change_password.html', {
        'form': form
    })
