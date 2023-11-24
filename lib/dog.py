#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __init__(self, name=""):
        self._name = None
        if name:
            self.set_name(name)

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 0 < len(value) <= 25:
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters.")

    name = property(get_name, set_name)


