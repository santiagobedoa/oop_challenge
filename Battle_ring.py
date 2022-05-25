#!/usr/bin/python3
from time import sleep


Pokemon = __import__('pokemon').Pokemon

def Battle(Pokemon_1, Pokemon_2):
    i = 1
    print(f"{(Pokemon_1.name).upper()} vs {(Pokemon_2.name).upper()}")
    while(True):
        print(f"---- Round {i} ----")
        sleep(2)
        f_attack = Pokemon_1.fight()
        Pokemon_2.damage(int(f_attack))
        print("{} receives: {} of damage, health remain: {}".format(Pokemon_2.name, f_attack, Pokemon_2.health))
        sleep(2)

        if Pokemon_2.health <= 0:
            print("{} wins the battle!".format(Pokemon_1.name))
            sleep(2)
            break

        f_attack = Pokemon_2.fight()
        Pokemon_1.damage(int(f_attack))
        print("{} receives: {} of damage, health remain: {}".format(Pokemon_1.name, f_attack, Pokemon_1.health))
        sleep(2)

        if Pokemon_1.health <= 0:
            print("{} wins the battle!".format(Pokemon_2.name))
            sleep(2)
            break
        print()
        i += 1
