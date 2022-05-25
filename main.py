#!/usr/bin/python3
from Battle_ring import Battle


Pokemon = __import__('pokemon').Pokemon

Charmander = Pokemon("Charmander", 4, "Fire", 0.6096, 8.482177, 5)
Corvisquire = Pokemon("Corvisquire", 822, "Flying", 0.8, 16.5, 6)
Battle(Charmander, Corvisquire)
