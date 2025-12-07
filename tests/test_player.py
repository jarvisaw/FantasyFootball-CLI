import pytest
from src.player import Player


def test_player_initialization():
    p = Player(
        id=1,
        name="Test Player",
        position="qb",
        team="KC",
        stats={"passing_yards": 300}
    )
    assert p.position == "QB"
    assert p.name == "Test Player"


def test_standard_scoring_qb():
    p = Player(
        id=1,
        name="QB Test",
        position="QB",
        team="KC",
        stats={
            "passing_yards": 300,   # 300 * 0.04 = 12
            "passing_tds": 2,       # 2 * 4 = 8
            "interceptions": 1      # -2
        }
    )
    assert p.calculate_fantasy_points() == pytest.approx(18.0)


def test_ppr_scoring():
    p = Player(
        id=2,
        name="WR Test",
        position="WR",
        team="DAL",
        stats={
            "receiving_yards": 100,  # 10 pts
            "receptions": 5          # 5 * 1.0 = 5 pts
        }
    )
    assert p.calculate_fantasy_points(ppr=1.0) == pytest.approx(15.0)


def test_missing_stats_defaults_to_zero():
    p = Player(
        id=3,
        name="No Stats",
        position="RB",
        team="SF",
        stats={}
    )
    assert p.calculate_fantasy_points() == 0.0