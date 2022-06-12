#!/usr/bin/python3
import numpy as np
from Battle_ring import Battle
import pypokedex as pokedex


Pokemon = __import__('pokemon').Pokemon
A = pokedex.get(dex=np.random.randint(1, 898))
B = pokedex.get(dex=np.random.randint(1, 898))

Pokemon_A = Pokemon(A.name, A.dex, A.types[0], A.height, A.weight, A.base_stats[0], A.base_stats[1])
Pokemon_B = Pokemon(B.name, B.dex, B.types[0], B.height, B.weight, B.base_stats[0], B.base_stats[1])
Battle(Pokemon_A, Pokemon_B)
