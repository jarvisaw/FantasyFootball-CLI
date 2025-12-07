# Fantasy Football CLI 🏈

![Tests](https://github.com/jarvisaw/FantasyFootball-CLI/actions/workflows/tests.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)

A professional command-line interface (CLI) tool for managing fantasy football player projections and statistics. This application allows users to view player data, search for specific athletes, and calculate fantasy scores based on customizable scoring rules (Standard vs. PPR).

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Testing](#testing)
- [AI-Assisted Development](#ai-assisted-development)
- [License](#license)

## Installation

1. **Clone the repository:**
```bash
   git clone https://github.com/jarvisaw/FantasyFootball-CLI.git
   cd FantasyFootball-CLI
```
2. **Create a virtual environment**
    * *On Windows:*
    ```bash
        python -m venv venv
        .\venv\Scripts\activate
    ```
    * *On macOS/Linux:*
    ```bash
        python3 -m venv venv
        source venv/bin/activate
    ```
3. **Install dependencies**
```bash
    pip install -r requirements.txt
```

---

## Usage
This application is run as a Python module. Below are the primary commands.

1. **List all players**
    Displays a formatted table of all players with their projected fantasy points.

```bash
    python -m src.main list
```
    Example outut:
```bash
    --- Fantasy Football CLI ---
    Listing players: All Players
    Total: 25
                    Player Projections
┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━┳━━━━━━┳━━━━━━━━━━━━━┓
┃ Name                ┃ Pos ┃ Team ┃ Fantasy Pts ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━╇━━━━━━╇━━━━━━━━━━━━━┩
│ Christian McCaffrey │ RB  │ SF   │       395.3 │
│ Josh Allen          │ QB  │ BUF  │      394.64 │
│ And so on...                                   |
```

Optional filters:
```bash
    python -m src.main list --position WR
    python -m src.main list --team KC
    python -m src.main list --top 10
    python -m src.main list --ppr 0.5
```

2. **Search for a player**
    Search for a specific player by name (case-insensitive)
```bash
    python -m src.main search "Mahomes"
```
```bash
    Found 1 matches for 'Mahomes':
    - Patrick Mahomes (KC, QB) => 364.3 pts
```

3. **View detailed scoring breakdown**
    Shows a full fantasy scoring breakdown for a single player:
```bash
    python -m src.main score "Josh Allen"
```
Supports custom PPR:
```bash
    python -m src.main score "Josh Allen" --ppr 0.5
```
Example output:
```bash
----- Fantasy Football CLI -----
----- Josh Allen (BUF, QB) -----
Passing Yards: 4306 -> 172.24 pts
Passing TDs: 29 -> 116.00 pts
Interceptions: 18 -> -36.00 pts
Rushing Yards: 524 -> 52.40 pts
Rushing TDs: 15 -> 90.00 pts

Total: 394.64 pts
```
---

## Features
* **Smart Scoring Engine:** Calculates fantasy points dynamically based on raw stats (passing/rushing/receiving yards and TDs).
* **Subcommand-based CLI:** Offers an engaging interface using
```bash 
    list 
    search
    score 
```
* **Rich Terminal UI:** Uses the rich library to render professional, colorful tables and formatted text.
* **Player Search:** Quickly filter the dataset to find specific targets.
* **CI/CD Pipeline:** Automated testing workflow via GitHub Actions ensures code stability on every push.
* **Robust Error Handling:** Gracefully handles missing data files or invalid user inputs.


---

## Testing
This project uses pytest for automated testing. To run the test suite:
```bash
pytest
```
Verbose output:
```bash
pytest -v
```

Tests include:
* Player scoring logic
* JSON loading
* CLI command execution

---

## AI-Assisted Development
This project was developed with assistance from AI tools including Google Gemini and GitHub Copilot.
For details on how AI contributed to architecture, debugging, and feature implementation, see AGENTS.md.

### License
This project is licensed under the MIT License — see the LICENSE file for details