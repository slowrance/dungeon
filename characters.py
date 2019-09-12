from __future__ import annotations

import random


class CharacterBase:
    def __init__(self, max_health: int,
                 level: int,
                 attack: float,
                 defense: float,
                 gold: int,
                 xp: int):

        self.curr_health = max_health
        self.max_health = max_health
        self.level = level
        self.att_str = attack
        self.def_str = defense
        self.gold = gold
        self.xp = xp

    def attack(self, other: CharacterBase):
        return self.attack_roll() >= other.defence_roll()

    def attack_roll(self):
        return self.att_str * random.random()

    def defence_roll(self):
        return self.def_str * random.random()


class Player(CharacterBase):
    def __init__(self, health=100, level=1, attack=10, defense=10, gold=0, xp=0):
        super(Player, self).__init__(health, level, attack, defense, gold, xp)

class MonsterFighter(CharacterBase):
    def __init__(self, health, level, attack, defense, gold, xp):
        super(MonsterFighter, self).__init__(health, level, attack, defense, gold, xp)
