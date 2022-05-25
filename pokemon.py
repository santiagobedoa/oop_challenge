#!/usr/bin/python3
import numpy as np


class Pokemon:
    """represents a Pokemon"""

    health = 15

    def __init__(self, name, number=0, p_type='', height=0, weight=0, attack=0):
        """initialize Pokemon attributes"""
        self.__name = name
        self.__number = number
        self.__p_type = p_type
        self.__height = height
        self.__weight = weight
        self.__attack = attack

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise TypeError("Pokemon's name must be letters")
        else:
            self.__name = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if type(value) is not int and int(value) < 0:
            raise TypeError("Pokemon's number must be integer")
        else:
            self.__number = value

    @property
    def p_type(self):
        return self.__p_type

    @p_type.setter
    def p_type(self, value):
        if type(value) is not str:
            raise TypeError("Pokemon's type must be letters")
        else:
            self.__p_type = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int and int(value) <= 0:
            raise TypeError("Pokemon's height must be a positive integer")
        else:
            self.__height = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if type(value) is not int and int(value) <= 0:
            raise TypeError("Pokemon's weight must be a positive integer")
        else:
            self.__weight = value

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, value):
        if type(value) is not int or value < 1:
            raise ValueError("Pokemon's attack must be a positive number")
        else:
            self.__attack = value
    
    def fight(self):
        attack_amount = int(round(self.__attack * np.random.random_sample(), 1))
        return attack_amount

    def damage(self, value):
        if type(value) is not int or value < 0:
            raise ValueError("Pokemon's damage must be a positive number")
        else:
            self.health -= value
