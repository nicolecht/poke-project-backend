from django.db import models
# from django.contrib.auth.models import User
# import random

class Pokemon(models.Model):
	name = models.CharField(max_length=100)
	hp = models.IntegerField()
	attack = models.IntegerField()
	defense = models.IntegerField()
	type = models.CharField(max_length=50)

	def __str__(self):
	    return self.name

# class Ownership(models.Model):
#     pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     level = models.IntegerField(default=random.randint(1, 100))

#     def __str__(self):
#         return f'{self.owner.username} owns {self.pokemon.name} (Level: {self.level})'

# we have created a new model called 'Ownership' that represents the relationship between a User and a Pokemon. The 'Ownership' model has a foreign key to both the 'User' and 'Pokemon' models, as well as a new field called 'level' that is randomly generated upon capture with a default value between 1 and 100.

# Note that we have also imported the 'User' model from Django's built-in authentication system, as we need it to create a foreign key relationship between a User and their owned Pokemon.

# After making these changes, you need to create the database tables for the new models by running the following command:

# python manage.py makemigrations
# python manage.py migrate

# Now, you can create ownership records in your views or using the Django shell like this:

# from django.contrib.auth.models import User
# from pokemon.models import Pokemon, Ownership

# # Assuming you have a user object and a pokemon object
# user = User.objects.first()
# pokemon = Pokemon.objects.first()

# # Create an ownership record for the user and pokemon
# ownership = Ownership.objects.create(pokemon=pokemon, owner=user)

# # Access the level of the ownership
# level = ownership.level

# Yes, we can make each Pokemon be owned by a single user and identified by a unique ID. To achieve this, we can modify the 'Ownership' model to include a unique constraint on the foreign key fields 'pokemon' and 'owner'. We can also add a new field called 'id_number' to the 'Ownership' model to uniquely identify each ownership record.

# Here's how the updated 'Ownership' model would look like:

# class Ownership(models.Model):
#     pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     level = models.IntegerField(default=random.randint(1, 100))
#     id_number = models.PositiveIntegerField(unique=True, editable=False)

#     def __str__(self):
#         return f'{self.owner.username} owns {self.pokemon.name} (Level: {self.level})'

#     def save(self, *args, **kwargs):
#         # Set the id_number field to a unique integer based on the current number of ownership records
#         count = Ownership.objects.count()
#         self.id_number = count + 1
#         super().save(*args, **kwargs)

#     class Meta:
#         unique_together = ('pokemon', 'owner')

# Here, we have added a new field called 'id_number' that is set to a unique integer value based on the current number of ownership records. We have also added a unique constraint to the 'Ownership' model that ensures that each combination of 'pokemon' and 'owner' is unique.

# Note that we have overridden the 'save' method of the 'Ownership' model to set the 'id_number' field to a unique value when a new ownership record is created.

# After making these changes, you need to create the database tables for the new model by running the following command:

# python manage.py makemigrations
# python manage.py migrate