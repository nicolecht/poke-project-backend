from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# import random
import uuid

class UserAccountManager(BaseUserManager):
	def create_user(self, username, password=None):
		if not username:
			raise ValueError('Users must have username')
		
		user = self.model(username=username)

		user.set_password(password)
		user.save()

		return user

class Pokemon(models.Model):
	name = models.CharField(max_length=100)
	hp = models.IntegerField()
	attack = models.IntegerField()
	defense = models.IntegerField()
	type = models.CharField(max_length=50)

	def __str__(self):
	    return self.name

class UserPokemon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pokemon = models.ManyToManyField(Pokemon)
    # level = models.PositiveIntegerField()
    # add other fields as needed

    def __str__(self):
        return f"{self.user.username} ({self.pokemon.count()} Pokemon)"
	
class BlacklistedToken(models.Model):
    # Define your fields here

    objects = models.Manager()