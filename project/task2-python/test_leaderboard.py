import pytest
from leaderboard import Leaderboard


def test_add_player():
    lb = Leaderboard()
    lb.add_player("Alice")
    assert len(lb) == 1


def test_add_player_with_initial_score():
    lb = Leaderboard()
    lb.add_player("Alice", initial_score=500)
    assert lb.get_top_n(1) == [("Alice", 500)]
    

def test_add_player_with_invalid_init():
    lb = Leaderboard()
    with pytest.raises(ValueError):
        lb.add_player("Cookies", initial_score=-1)

def test_add_player_already_registered():
    lb = Leaderboard()
    lb.add_player("Alice", initial_score=500)
    with pytest.raises(ValueError):
        lb.add_player("Alice", initial_score=100)

def test_record_match_unregistered_loser():
    lb = Leaderboard()
    lb.add_player("Alice", 100)
    with pytest.raises(KeyError):
        lb.record_match("Alice", "Ghost")

def test_record_match_unregistered_winner():
    lb = Leaderboard()
    lb.add_player("Alice", 100)
    with pytest.raises(KeyError):
        lb.record_match("Ghost", "Alice")

def test_record_match_invalid_points():
    lb = Leaderboard()
    lb.add_player("Alice", 100)
    lb.add_player("Ghost", 100)
    with pytest.raises(ValueError):
        lb.record_match("Alice", "Ghost", -10)

def test_get_rank_invalid_player():
    lb = Leaderboard()
    with pytest.raises(KeyError):
        lb.get_rank("Alice")

def test_negative_top_n():
    lb = Leaderboard()
    with pytest.raises(ValueError):
        lb.get_top_n(-1)

def test_get_percentile():
    lb = Leaderboard()
    with pytest.raises(KeyError):
        lb.get_percentile("Alice")
    lb.add_player("Alice", 500)
    assert lb.get_percentile("Alice") == 100.0
    lb.add_player("Cookies", 700)
    assert lb.get_percentile("Alice") == 0.0

def test_apply_bonus():
    lb = Leaderboard()
    with pytest.raises(KeyError):
        lb.apply_bonus("Alice", 1.5)
    lb.add_player("Alice", 500)
    with pytest.raises(ValueError):
        lb.apply_bonus("Alice", -1.5)
    lb.apply_bonus("Alice", 1.5)
    assert lb.get_top_n(1) == [("Alice", 750)]

def test_get_winrate():
    lb = Leaderboard()
    with pytest.raises(KeyError):
        lb.get_win_rate("Alice")
    lb.add_player("Alice", 500)
    lb.add_player("Cookies", 700)
    assert lb.get_win_rate("Cookies") == 0.0
    lb.record_match("Cookies", "Alice", 10)
    assert lb.get_win_rate("Cookies") == 1.0

def test_reset():
    lb = Leaderboard()
    lb.add_player("Alice")
    assert len(lb) == 1
    lb.reset()
    assert len(lb) == 0

def test_record_match_updates_scores():
    lb = Leaderboard()
    lb.add_player("Alice", 100)
    lb.add_player("Bob", 100)
    lb.record_match("Alice", "Bob")
    assert lb.get_top_n(2) == [("Alice", 110), ("Bob", 90)]


def test_get_rank():
    lb = Leaderboard()
    lb.add_player("Alice", 300)
    lb.add_player("Bob", 100)
    lb.add_player("Carol", 200)
    assert lb.get_rank("Alice") == 1
    assert lb.get_rank("Carol") == 2
    assert lb.get_rank("Bob") == 3
