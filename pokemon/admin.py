from django.contrib import admin
from .models import Pokemon, UserPokemon

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(UserPokemon)