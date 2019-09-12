from game import Game
from characters import Player


def test_new_game():
    game = Game()
    game.turns = 2
    assert game.turns > 0
    game = Game()
    assert game.turns == 0
