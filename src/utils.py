# src/utils.py
import json
import os
from src.player import Player

def load_players(file_path):
    """
    Loads player data from a JSON file and returns a list of Player objects.
    """
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' was not found.")
        return []

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            
            players = []
            for item in data:
                # Create a Player object for each dictionary in the JSON
                player = Player(
                    item['id'],
                    item['name'],
                    item['position'],
                    item['team'],
                    item['bye_week'],
                    item['projected_points']
                )
                players.append(player)
            
            return players
            
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' contains invalid JSON.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []