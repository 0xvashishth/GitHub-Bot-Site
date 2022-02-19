from django import forms
from .models import users,orders


class UsersForm(forms.ModelForm):

	class Meta:

		model = users

		fields=[
			"name",
			"email",
			"phone",
			"password",
			"githubid",
			"token",
		]