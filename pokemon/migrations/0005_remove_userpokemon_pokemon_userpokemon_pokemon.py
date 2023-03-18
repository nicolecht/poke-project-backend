# Generated by Django 4.1.7 on 2023-03-18 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0004_remove_userpokemon_pokemon_userpokemon_pokemon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpokemon',
            name='pokemon',
        ),
        migrations.AddField(
            model_name='userpokemon',
            name='pokemon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pokemon.pokemon'),
        ),
    ]
