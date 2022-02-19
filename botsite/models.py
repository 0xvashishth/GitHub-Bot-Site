from django.db import models
import uuid



class users(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False)
	name = models.CharField(max_length=250)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	password = models.CharField(max_length=25)
	githubid = models.CharField(max_length=50)
	token = models.CharField(max_length=200)


class orders(models.Model):
	user_id = models.CharField(max_length=300)
	date = models.CharField(max_length=100)
	token = models.CharField(max_length=200)