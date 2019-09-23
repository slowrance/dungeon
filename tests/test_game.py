from game import Game
from characters import Player


def test_new_game():
    game = Game()
    game.turns = 2
    assert game.turns > 0
    game = Game()
    assert game.turns == 0

def test_locations(new_game):
    game = new_game
    assert game.locations == ['forest', 'town', 'shop']


def test_look_around_event():
    pass

def test_look_around_opponent():
    pass

def test_rest_safely():
    pass

def test_rest_danger():
    pass
