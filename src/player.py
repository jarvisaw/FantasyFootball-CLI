# src/player.py

class Player:
    def __init__(self, id, name, position, team, bye_week, projected_points):
        self.id = id
        self.name = name
        self.position = position
        self.team = team
        self.bye_week = bye_week
        self.projected_points = projected_points

    def __str__(self):
        """Returns a string representation of the player."""
        return f"{self.name} ({self.position} - {self.team}) | Proj: {self.projected_points}"

    def to_dict(self):
        """Converts player object back to dictionary (useful for saving)."""
        return {
            "id": self.id,
            "name": self.name,
            "position": self.position,
            "team": self.team,
            "bye_week": self.bye_week,
            "projected_points": self.projected_points
        }