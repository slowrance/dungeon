class Game:
    def __init__(self):
        self.turns = 0
        self.kills = 0
        self.game_end = False

    def start_game(self):
        while not self.game_end:
            self.get_action()

    def get_action(self, location):
        pass
