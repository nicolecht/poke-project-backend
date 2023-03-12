import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'poke_project.settings')

import django
django.setup()

import csv
from pokemon.models import Pokemon

count = 0

with open('pokemon.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        name = row[0]
        hp = row[1]
        attack = row[2]
        defense = row[3]
        type = row[4]
        try:
            pokemon = Pokemon.objects.create(
                name=name,
                hp=int(hp),
                attack=int(attack),
                defense=int(defense),
                type=type,
            )
            print("Successfully created " + name)
            count += 1
        except ValueError as e:
            print("Error creating " + name + ": " + str(e))

print("Created " + str(count) + " Pokemon records.")
