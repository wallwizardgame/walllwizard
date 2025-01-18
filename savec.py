import json

def save_game_data(game_data, file_path):
    """bsort json file save mishe ."""
    try:
        with open(file_path, 'r') as file:
            games = json.load(file)
    except FileNotFoundError:
        games = []

    games.append(game_data)

    with open(file_path, 'w') as file:
        json.dump(games, file, indent=4)

def record_game():
    """sbt etelaat new game."""
    game_data = {
        "game_id": input("Enter game ID: "),
        "player1": input("Enter Player 1 Name: "),
        "player2": input("Enter Player 2 Name: "),
        "player1_position": input("Enter Player 1 Position: "),
        "player2_position": input("Enter Player 2 Position: "),
        "wall_positions": input("Enter Wall Positions (e.g., [(x1, y1), (x2, y2)]): "),
        "current_turn": input("Whose turn is it (Player 1/Player 2)?: "),
        "time_spent": int(input("Enter total time spent (in minutes): ")),
        "result": input("Enter result (e.g., Player 1 wins): ")
    }

    save_game_data(game_data, "games_data.json")
    print("Game data saved successfully!")

# estfade az tabe
if name == "main":
    record_game()

save_game_data

def save_game_data(game_data, file_path):
    """Save game data to a JSON file."""

    try:
        with open(file_path, 'r') as file:
            games = json.load(file)
    except FileNotFoundError:
        games = []


    games.append(game_data)


    with open(file_path, 'w') as file:
        json.dump(games, file, indent=4)


def record_game():
    """Record a new game's data."""



    game_data = {
        "game_id": input("Enter game ID: "),
        "player1": input("Enter Player 1 Name: "),
        "player2": input("Enter Player 2 Name: "),
        "player1_position": input("Enter Player 1 Position: "),
        "player2_position": input("Enter Player 2 Position: "),
        "wall_positions": input("Enter Wall Positions (e.g., [(x1, y1), (x2, y2)]): "),
        "current_turn": input("Whose turn is it (Player 1/Player 2)?: "),
        "time_spent": int(input("Enter total time spent (in minutes): ")),
        "result": input("Enter result (e.g., Player 1 wins): ")
    }


    save_game_data(game_data, "games_data.json")
    print("Game data saved successfully!")



if name == "main":
    record_game()