from django.test import TestCase
from .models import Pokemon, CapturedPokemon
from django.contrib.auth.models import User

class CapturedPokemonTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.original_pokemon = Pokemon.objects.first()

    def test_capture_pokemon(self):
        captured_pokemon = CapturedPokemon.capture(self.user, self.original_pokemon)

        # Check that a new captured Pokemon instance has been created
        self.assertIsNotNone(captured_pokemon.id)

        # Check that the captured Pokemon has the correct attributes
        self.assertEqual(captured_pokemon.user, self.user)
        self.assertEqual(captured_pokemon.original_pokemon, self.original_pokemon)
        self.assertEqual(captured_pokemon.hp, self.original_pokemon.hp)
        self.assertEqual(captured_pokemon.attack, self.original_pokemon.attack)
        self.assertEqual(captured_pokemon.defense, self.original_pokemon.defense)
        self.assertEqual(captured_pokemon.type, self.original_pokemon.type)
