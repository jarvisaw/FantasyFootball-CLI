import json
import tempfile
from src.utils import load_players
from src.player import Player


def test_load_players_creates_player_objects():
    sample_data = [
        {
            "id": 1,
            "name": "Test Player",
            "position": "QB",
            "team": "KC",
            "stats": {"passing_yards": 100}
        }
    ]

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        json.dump(sample_data, tmp)
        tmp_path = tmp.name

    players = load_players(tmp_path)

    assert len(players) == 1
    assert isinstance(players[0], Player)
    assert players[0].name == "Test Player"


def test_load_players_file_not_found():
    try:
        load_players("nonexistent_file.json")
        assert False, "Expected FileNotFoundError"
    except FileNotFoundError:
        assert True