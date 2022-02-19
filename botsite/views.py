from django.shortcuts import render
from django import forms
from .forms import UsersForm
# from . import forms
from .models import users,orders


def list_users(request):

	context = {}
	context["dataset"]=users.objects.all()

	return render(request,"list_users.html",context)



def create_users(request):

	context={}

	form = UsersForm(request.POST or None)

	if form.is_valid():
		form.save()


	context['form']= form
	return render(request,"create_users.html", context)