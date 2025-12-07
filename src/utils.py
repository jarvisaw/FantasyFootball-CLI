import json
from typing import List
from src.player import Player

def load_players(file_path: str) -> List[Player]:
    """
    Reads a JSON file and converts it into a list of Player objects.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            
        players = []
        for entry in data:
            # We explicitly map the JSON fields to the Player class
            player = Player(
                id=entry['id'],
                name=entry['name'],
                position=entry['position'],
                team=entry['team'],
                stats=entry.get('stats', {})
            )
            players.append(player)
            
        return players
    
    except FileNotFoundError:
        # In a real app, you might want to log this or raise a custom error
        raise
    except json.JSONDecodeError:
        print(f"Error: {file_path} contains invalid JSON.")
        return []