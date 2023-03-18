from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from pokemon.models import Pokemon, UserPokemon

class UserPokemonViewTestCase(APITestCase):
    def setUp(self):
        # create test data
        self.user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')
        self.pokemon1 = Pokemon.objects.create(name='Pikachu', hp=100, attack=100, defense=100)
        self.pokemon2 = Pokemon.objects.create(name='Charizard', hp=100, attack=100, defense=100)
        self.user_pokemon1 = UserPokemon.objects.create(user=self.user, pokemon=self.pokemon1)
        self.user_pokemon2 = UserPokemon.objects.create(user=self.user, pokemon=self.pokemon2)

    def test_user_pokemon_view(self):
        # simulate a GET request to the user pokemon view for the test user
        self.client.force_login(self.user)
        response = self.client.get('/user_pokemon/')
        
        # assert that the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # assert that the response data includes the test user's pokemon
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['user'], self.user.id)
        self.assertEqual(response.data[0]['pokemon'], self.pokemon1.id)
        # self.assertEqual(response.data[0]['level'], 10)
        self.assertEqual(response.data[1]['user'], self.user.id)
        self.assertEqual(response.data[1]['pokemon'], self.pokemon2.id)
        # self.assertEqual(response.data[1]['level'], 20)
