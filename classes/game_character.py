# Build a Game Character Stats Tracker

"""Represent a character and the stats that can change during a game.
The character starts at level 1 with full health and mana. Health is kept in
the inclusive range 0-100, while mana is kept in the inclusive range 0-50.
"""
class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._level = 1
        self._health = 100
        self._mana = 50

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = max(0, min(value, 100))

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        self._mana = max(0, min(value, 50))

    # Advance one level and restore health and mana to their maximums
    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Level: {self.level}\n"
            f"Health: {self.health}\n"
            f"Mana: {self.mana}"
        )
