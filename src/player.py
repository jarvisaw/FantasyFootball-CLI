from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Player:
    id: int
    name: str
    position: str
    team: str
    stats: Dict[str, float] = field(default_factory=dict)

    def __post_init__(self):
        # normalize position to uppercase just in case
        self.position = self.position.upper()

    def calculate_fantasy_points(self, ppr: float = 1.0) -> float:
        """
        Calculates fantasy points based on standard scoring.
        ppr: Points Per Reception (default 1.0)
        """
        score = 0.0
        s = self.stats

        # Offensive Scoring Standard
        score += s.get("passing_yards", 0) * 0.04
        score += s.get("passing_tds", 0) * 4.0
        score += s.get("interceptions", 0) * -2.0
        
        score += s.get("rushing_yards", 0) * 0.1
        score += s.get("rushing_tds", 0) * 6.0
        
        score += s.get("receiving_yards", 0) * 0.1
        score += s.get("receiving_tds", 0) * 6.0
        score += s.get("receptions", 0) * ppr
        
        score += s.get("fumbles_lost", 0) * -2.0

        return round(score, 2)

    def __str__(self):
        return f"{self.name} ({self.position} - {self.team})"