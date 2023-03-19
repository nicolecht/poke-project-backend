# Generated by Django 4.1.7 on 2023-03-19 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0016_alter_userpokemon_pokemon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpokemon',
            name='pokemon',
            field=models.ManyToManyField(limit_choices_to={'user': models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)}, to='pokemon.capturedpokemons'),
        ),
    ]
