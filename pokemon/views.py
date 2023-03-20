from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from pokemon.serializers import UserPokemonSerializer, PokemonSerializer, AddAndReleasePokemonSerializer
from pokemon.models import UserPokemon, Pokemon
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import generics, status

class UnownedPokemonView(APIView):
    def get(self, request):
        # Retrieve the user from the request (e.g. using request.user)
        user = request.user
        # Retrieve all the Pokemon objects that the user does not own
        unowned_pokemon = Pokemon.objects.exclude(userpokemon__user=user)
        serializer = PokemonSerializer(unowned_pokemon, many=True)
        return Response(serializer.data)

class UserPokemonView(APIView):
    def get(self, request):
        # retrieve the user from the request (e.g. using request.user)
        # user = get_object_or_404(User, username=username)
        user = request.user
        user_pokemon = UserPokemon.objects.filter(user=user)
        serializer = UserPokemonSerializer(user_pokemon, many=True)
        return Response(serializer.data)

class AddPokemonView(APIView):
    def post(self, request):
        user = request.user
        # assume the pokemon name is sent as JSON in the request body
        serializer = AddAndReleasePokemonSerializer(data=request.data)
        if serializer.is_valid():
            pokemon_data = serializer.validated_data
            try:
                # retrieve the Pokemon object from the database using the name field
                pokemon = Pokemon.objects.get(name=pokemon_data['name'])
                # retrieve the UserPokemon object for the current user, if it exists
                user_pokemon = UserPokemon.objects.get(user=user)
            except (UserPokemon.DoesNotExist):
                # if either the Pokemon or UserPokemon object does not exist, create a new UserPokemon object
                user_pokemon = UserPokemon()
                user_pokemon.user = user
                user_pokemon.save()
            # add the pokemon to the UserPokemon object and save it
            user_pokemon.pokemon.add(pokemon)
            # serialize the UserPokemon object and return it in the response
            user_pokemon_serializer = UserPokemonSerializer(user_pokemon)
            return Response(user_pokemon_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReleasePokemonView(APIView):
    def post(self, request):
        user = request.user
        # assume the pokemon name is sent as JSON in the request body
        serializer = AddAndReleasePokemonSerializer(data=request.data)
        if serializer.is_valid():
            pokemon_data = serializer.validated_data
            try:
                # retrieve the Pokemon object from the database using the name field
                pokemon = Pokemon.objects.get(name=pokemon_data['name'])
                # retrieve the UserPokemon object for the current user, if it exists
                user_pokemon = UserPokemon.objects.get(user=user)
            except (Pokemon.DoesNotExist, UserPokemon.DoesNotExist):
                # if either the Pokemon or UserPokemon object does not exist, return an error response
                return Response({'error': 'Invalid Pokemon or User'}, status=status.HTTP_400_BAD_REQUEST)
            # remove the pokemon from the UserPokemon object and save it
            user_pokemon.pokemon.remove(pokemon)
            # serialize the UserPokemon object and return it in the response
            user_pokemon_serializer = UserPokemonSerializer(user_pokemon)
            return Response(user_pokemon_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllPokemonAPIView(generics.ListAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')