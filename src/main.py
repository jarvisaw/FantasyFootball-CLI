# src/main.py

import argparse
import sys
from pathlib import Path
from typing import List, Optional

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from src.utils import load_players
from src.player import Player


console = Console()


def resolve_data_path(relative_path: str) -> Path:
    """Resolve the data file path relative to project root."""
    base_path = Path(__file__).parent.parent
    return base_path / relative_path


def load_player_data(file_path: str) -> List[Player]:
    """Load players from JSON, with error handling."""
    data_path = resolve_data_path(file_path)

    try:
        players = load_players(str(data_path))
    except FileNotFoundError:
        console.print(f"[bold red]Error:[/bold red] Could not find data file at {data_path}")
        sys.exit(1)

    if not players:
        console.print(f"[bold red]Error:[/bold red] No players loaded from {data_path}")
        sys.exit(1)

    return players


def filter_players(
    players: List[Player],
    position: Optional[str] = None,
    team: Optional[str] = None,
) -> List[Player]:
    """Filter players by position and/or team."""
    filtered = players

    if position:
        position = position.upper()
        filtered = [p for p in filtered if p.position == position]

    if team:
        team = team.upper()
        filtered = [p for p in filtered if p.team.upper() == team]

    return filtered


def sort_and_limit_players(
    players: List[Player],
    ppr: float,
    top: Optional[int] = None,
) -> List[Player]:
    """Sort players by fantasy points (desc) and optionally take top N."""
    sorted_players = sorted(
        players,
        key=lambda p: p.calculate_fantasy_points(ppr=ppr),
        reverse=True,
    )
    if top is not None and top > 0:
        sorted_players = sorted_players[:top]
    return sorted_players


# -----------------------------
# Subcommand: list
# -----------------------------
def handle_list(args: argparse.Namespace) -> None:
    players = load_player_data(args.file)

    filtered_players = filter_players(
        players,
        position=args.position,
        team=args.team,
    )

    if not filtered_players:
        console.print("\n[red]No players found with the given filters.[/red]\n")
        return

    filtered_players = sort_and_limit_players(
        filtered_players,
        ppr=args.ppr,
        top=args.top,
    )

    # Build description of filters
    filters_desc_parts = []
    if args.position:
        filters_desc_parts.append(f"Pos={args.position.upper()}")
    if args.team:
        filters_desc_parts.append(f"Team={args.team.upper()}")
    if args.top:
        filters_desc_parts.append(f"Top={args.top}")

    filters_desc = " | ".join(filters_desc_parts) if filters_desc_parts else "All Players"

    console.print("\n[bold green]Fantasy Football CLI[/bold green]", justify="center")
    console.print("-" * 40, justify="center")
    console.print(f"\n[bold]Listing players:[/bold] {filters_desc}")
    console.print(f"Total: [cyan]{len(filtered_players)}[/cyan]\n")

    table = Table(title="Player Projections")

    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Pos", style="magenta")
    table.add_column("Team", style="green")
    table.add_column("Fantasy Pts", justify="right", style="yellow")

    for p in filtered_players:
        pts = p.calculate_fantasy_points(ppr=args.ppr)
        table.add_row(p.name, p.position, p.team, str(pts))

    console.print(table)


# -----------------------------
# Subcommand: search
# -----------------------------
def handle_search(args: argparse.Namespace) -> None:
    players = load_player_data(args.file)

    query = args.query.lower()
    results = [p for p in players if query in p.name.lower()]

    console.print("\n[bold green]Fantasy Football CLI[/bold green]", justify="center")
    console.print("-" * 40, justify="center")

    if not results:
        console.print(f"\n[red]No players found matching '{args.query}'[/red]\n")
        return

    console.print(f"\nFound [cyan]{len(results)}[/cyan] matches for '{args.query}':\n")

    for p in results:
        pts = p.calculate_fantasy_points(ppr=args.ppr)
        console.print(
            f" - [bold]{p.name}[/bold] ({p.team}, {p.position}) "
            f"=> [yellow]{pts} pts[/yellow]"
        )


# -----------------------------
# Subcommand: score
# -----------------------------
def handle_score(args: argparse.Namespace) -> None:
    players = load_player_data(args.file)

    query = args.player_name.lower()
    matches = [p for p in players if query in p.name.lower()]

    console.print("\n[bold green]Fantasy Football CLI[/bold green]", justify="center")
    console.print("-" * 40, justify="center")

    if not matches:
        console.print(f"\n[red]No players found matching '{args.player_name}'[/red]\n")
        return

    if len(matches) > 1:
        console.print(
            f"\n[yellow]Multiple players matched '{args.player_name}'. "
            "Please be more specific:[/yellow]\n"
        )
        for p in matches:
            console.print(f" - [bold]{p.name}[/bold] ({p.team}, {p.position})")
        return

    player = matches[0]
    s = player.stats
    ppr = args.ppr

    total = player.calculate_fantasy_points(ppr=ppr)

    lines = []

    # Passing
    if "passing_yards" in s:
        lines.append(f"Passing Yards: {s['passing_yards']} -> {s['passing_yards'] * 0.04:.2f} pts")
    if "passing_tds" in s:
        lines.append(f"Passing TDs: {s['passing_tds']} -> {s['passing_tds'] * 4.0:.2f} pts")
    if "interceptions" in s:
        lines.append(f"Interceptions: {s['interceptions']} -> {s['interceptions'] * -2.0:.2f} pts")

    # Rushing
    if "rushing_yards" in s:
        lines.append(f"Rushing Yards: {s['rushing_yards']} -> {s['rushing_yards'] * 0.1:.2f} pts")
    if "rushing_tds" in s:
        lines.append(f"Rushing TDs: {s['rushing_tds']} -> {s['rushing_tds'] * 6.0:.2f} pts")

    # Receiving
    if "receiving_yards" in s:
        lines.append(f"Receiving Yards: {s['receiving_yards']} -> {s['receiving_yards'] * 0.1:.2f} pts")
    if "receiving_tds" in s:
        lines.append(f"Receiving TDs: {s['receiving_tds']} -> {s['receiving_tds'] * 6.0:.2f} pts")
    if "receptions" in s:
        lines.append(f"Receptions: {s['receptions']} x {ppr} PPR -> {s['receptions'] * ppr:.2f} pts")

    # Fumbles
    if "fumbles_lost" in s:
        lines.append(f"Fumbles Lost: {s['fumbles_lost']} -> {s['fumbles_lost'] * -2.0:.2f} pts")

    body = "\n".join(lines) if lines else "No recorded stats for this player."

    panel = Panel(
        f"{body}\n\n[bold]Total:[/bold] {total:.2f} pts",
        title=f"{player.name} ({player.team}, {player.position})",
        subtitle=f"PPR: {ppr}",
        border_style="cyan",
    )

    console.print(panel)


# -----------------------------
# Main entry: argparse setup
# -----------------------------
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Fantasy Football CLI Tool",
    )

    parser.add_argument(
        "--file",
        default="data/players.json",
        help="Path to player data file (default: data/players.json)",
    )

    subparsers = parser.add_subparsers(
        title="Commands",
        dest="command",
        required=True,
    )

    # list command
    list_parser = subparsers.add_parser(
        "list",
        help="List players with fantasy scores",
    )
    list_parser.add_argument("--position", type=str)
    list_parser.add_argument("--team", type=str)
    list_parser.add_argument("--top", type=int)
    list_parser.add_argument("--ppr", type=float, default=1.0)
    list_parser.set_defaults(func=handle_list)

    # search command
    search_parser = subparsers.add_parser(
        "search",
        help="Search for players by name",
    )
    search_parser.add_argument("query", type=str)
    search_parser.add_argument("--ppr", type=float, default=1.0)
    search_parser.set_defaults(func=handle_search)

    # score command
    score_parser = subparsers.add_parser(
        "score",
        help="Show detailed fantasy scoring breakdown for a single player",
    )
    score_parser.add_argument("player_name", type=str)
    score_parser.add_argument("--ppr", type=float, default=1.0)
    score_parser.set_defaults(func=handle_score)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()