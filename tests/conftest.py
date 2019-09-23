import pytest
from characters import CharacterBase
from game import Game


@pytest.fixture
def generic_characters():
    a = CharacterBase()
    b = CharacterBase()
    return a, b

@pytest.fixture
def new_game():
    game = Game()
    return game
