from django.shortcuts import render
from django import forms
from .forms import UsersForm
from django.http import HttpResponseRedirect
# from . import forms
from django.shortcuts import get_list_or_404, get_object_or_404
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
		return HttpResponseRedirect("/")


	context['form']= form
	return render(request,"create_users.html", context)


def detail_users(request,id):

	context={}
	context['data']=users.objects.get(id = id)
	return render(request,"detail_users.html", context)


def update_users(request,id):

	context={}
	obj = get_object_or_404(users,id=id)

	form = UsersForm(request.POST or None , instance = obj)


	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/"+id)


	context["form"] = form

	return render(request, "update_users.html", context)



def delete_users(request,id):

	context = {}

	obj = get_object_or_404(users, id=id)

	if request.method == "POST":
		obj.delete()

		return HttpResponseRedirect("/")


	return render(request, "delete_users.html", context)