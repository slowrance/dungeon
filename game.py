class Game:
    def __init__(self):
        self.turns = 0
        self.kills = 0
        self.game_end = False
        self.locations = self.generate_locations()

    def start_game(self):
        while not self.game_end:
            self.get_action()

    def get_action(self, location):
        pass
