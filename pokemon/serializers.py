from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from pokemon.models import UserPokemon, Pokemon

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
	class Meta(UserCreateSerializer.Meta):
		model = User
		fields = ('username', 'password')

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'hp', 'attack', 'defense', 'type']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class UserPokemonSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    pokemon = PokemonSerializer(many=True)

    class Meta:
        model = UserPokemon
        fields = ['id', 'user', 'pokemon']

class AddAndReleasePokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['name']
