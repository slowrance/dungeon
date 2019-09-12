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


def test_attack_hit():
    attacker = Player()
    defender = MonsterFighter(100, 1, 10, 10, 0, 0)
    result = attacker.attack(defender)
    assert result

def test_attack_miss():
    pass
