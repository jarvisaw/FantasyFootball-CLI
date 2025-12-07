# tests/test_player.py
import pytest
from src.player import Player
from src.utils import load_players

def test_player_creation():
    """Test that a Player object is created with correct attributes."""
    p = Player(1, "Test Player", "QB", "TST", 10, 20.5)
    
    assert p.name == "Test Player"
    assert p.position == "QB"
    assert p.projected_points == 20.5

def test_player_string_representation():
    """Test the __str__ method for nice printing."""
    p = Player(1, "Joe Burrow", "QB", "CIN", 10, 22.0)
    expected_str = "Joe Burrow (QB - CIN) | Proj: 22.0"
    
    assert str(p) == expected_str

def test_load_players_file_not_found():
    """Test that loading a non-existent file returns an empty list (no crash)."""
    result = load_players("data/fake_file.json")
    
    # It should return an empty list, not crash with an error
    assert result == []
    assert len(result) == 0