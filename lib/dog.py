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
    def __init__(self, name="", breed=""):
        self._name = name
        self._breed = breed


    def get_name(self):
        return self._name

    def set_name(self, value):
        if (type(value) in str) and 0 < len(value) <= 25:
            self._name = value
            print(value)
        else:
            print("Name must be a string between 1 and 25 characters.")

    def get_breed(self):
        return self._breed

    def set_breed(self, value):
        approved_breeds = ["Pug", "Labrador", "Golden Retriever"]  # Add more breeds as needed
        if value in approved_breeds:
            self._breed = value
        else:
            print("Breed must be in the list of approved breeds.")

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)

fido = Dog("fido")