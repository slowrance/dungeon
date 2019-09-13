from __future__ import annotations

import random


class CharacterBase:
    def __init__(self, max_health: int = 100,
                 level: int = 1,
                 attack: float = 10,
                 defense: float = 10,
                 gold: int = 0,
                 xp: int = 0):

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

    def deal_damage(self, other):
        other.curr_health -= random.randint(1, self.damage)


class Player(CharacterBase):
    def __init__(self):
        super(Player, self).__init__()


class MonsterFighter(CharacterBase):
    def __init__(self):
        super(MonsterFighter, self).__init__()
