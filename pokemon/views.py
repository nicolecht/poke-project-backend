from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from pokemon.serializers import UserPokemonSerializer, PokemonSerializer
from pokemon.models import UserPokemon, Pokemon
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import generics

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