class CharacterBase:
    def __init__(self):
        self.health = 0
        self.level = 0
        self.attack = 0
        self.defense = 0

class Player(CharacterBase):
    def __init__(self):
        super(Player, self).__init__()
        self.xp = 0


