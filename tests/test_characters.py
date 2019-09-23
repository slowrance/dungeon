from unittest.mock import patch

from characters import CharacterBase, Player, MonsterFighter
from tests.conftest import generic_characters



def test_base_character_properties(generic_characters):
    a, _ = generic_characters
    assert hasattr(a, 'max_health')
    assert hasattr(a, 'curr_health')
    assert hasattr(a, 'level')
    assert hasattr(a, 'att_str')
    assert hasattr(a, 'def_str')
    assert hasattr(a, 'gold')
    assert hasattr(a, 'xp')


def test_player_properties():
    player = Player()
    assert hasattr(player, 'xp')
    assert hasattr(player, 'gold')


@patch.object(CharacterBase, 'attack_roll')
@patch.object(CharacterBase, 'defence_roll')
def test_attack_hit(a, d):
    attacker = Player()
    defender = MonsterFighter()
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
        defender = MonsterFighter()
        attacker.attack_roll.return_value = 2
        defender.defence_roll.return_value = 9
        hit = attacker.attack(defender)
        assert not hit


def test_deal_damage(generic_characters):
    attacker, defender = generic_characters
    attacker.damage = 5
    defender.max_health = 100
    defender.curr_health = 100
    assert defender.curr_health == 100
    attacker.deal_damage(defender)
    assert defender.curr_health < 100


def test_player_kill_monster():
    player = Player()
    player.xp = 0
    player.xp = 0
    player.damage = 5
    monster = MonsterFighter()
    monster.curr_health = 1
    monster.xp = 10
    monster.gold = 10
    player.deal_damage(monster)
    assert player.xp == 10
    assert player.gold == 10


