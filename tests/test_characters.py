import pytest

from characters.characters import CharacterBase, Player

def test_base_character_properties():
    cb = CharacterBase()
    assert hasattr(cb, 'health')
    assert hasattr(cb, 'level')
    assert hasattr(cb, 'attack')
    assert hasattr(cb, 'defense')

def test_player_properties():
    player = Player()
    assert hasattr(player, 'health')
    assert hasattr(player, 'level')
    assert hasattr(player, 'attack')
    assert hasattr(player, 'defense')
    assert hasattr(player, 'xp')



