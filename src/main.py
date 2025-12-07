# src/main.py
from src.utils import load_players

def main():
    print("--- Fantasy Football CLI ---")
    
    # Load the data
    players = load_players('data/players.json')
    
    print(f"Successfully loaded {len(players)} players:")
    for player in players:
        print(f" - {player}")

if __name__ == "__main__":
    main()