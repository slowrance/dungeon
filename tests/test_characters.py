from unittest.mock import patch

from characters import CharacterBase, Player, MonsterFighter


def test_base_character_properties():
    cb = CharacterBase(100, 1, 10, 10, 0, 2)
    assert hasattr(cb, 'max_health')
    assert hasattr(cb, 'curr_health')
    assert hasattr(cb, 'level')
    assert hasattr(cb, 'att_str')
    assert hasattr(cb, 'def_str')
    assert hasattr(cb, 'gold')
    assert hasattr(cb, 'xp')


def test_player_properties():
    player = Player(100, 1, 10, 10, 0, 0)
    assert hasattr(player, 'xp')
    assert hasattr(player, 'gold')


def test_monster_properties():
    pass


@patch.object(CharacterBase, 'attack_roll')
@patch.object(CharacterBase, 'defence_roll')
def test_attack_hit(a, d):
    attacker = Player()
    defender = MonsterFighter(100, 1, 10, 10, 0, 0)
    attacker.attack_roll.return_value = 9
    defender.defence_roll.return_value = 2
    hit = attacker.attack(defender)
    assert hit
    attacker.attack_roll.return_value = 2
    defender.defence_roll.return_value = 2
    hit = attacker.attack(defender)
    assert hit


def test_attack_miss():
    @patch.object(CharacterBase, 'attack_roll')
    @patch.object(CharacterBase, 'defence_roll')
    def test_attack_mi(a, d):
        attacker = Player()
        defender = MonsterFighter(100, 1, 10, 10, 0, 0)
        attacker.attack_roll.return_value = 2
        defender.defence_roll.return_value = 9
        hit = attacker.attack(defender)
        assert not hit
