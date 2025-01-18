import json
import re
import uuid
import quoridor2
import bcrypt
import saving
from colorama import Fore, Style

USERS_FILE = "users.json"
GAMES_FILE = "games.json"

DEFAULT_BOARD = [["   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   "] 
            , [" -  "," -  "," -  "," -  "," -  "," -  "," -  "," -  "," - "] 
            , ["   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   "] 
            , [" -  "," -  "," -  "," -  "," -  "," -  "," -  "," -  "," - "] 
            , ["   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   "] 
            , [" -  "," -  "," -  "," -  "," -  "," -  "," -  "," -  "," - "] 
            , ["   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   "] 
            , [" -  "," -  "," -  "," -  "," -  "," -  "," -  "," -  "," - "] 
            , ["   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   "] 
            , [" -  "," -  "," -  "," -  "," -  "," -  "," -  "," -  "," - "] 
            , ["   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   "] 
            , [" -  "," -  "," -  "," -  "," -  "," -  "," -  "," -  "," - "] 
            , ["   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   "] 
            , [" -  "," -  "," -  "," -  "," -  "," -  "," -  "," -  "," - "] 
            , ["   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   "] 
            , [" -  "," -  "," -  "," -  "," -  "," -  "," -  "," -  "," - "] 
            , ["   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   "]]


def load_users():
    try:
        with open(USERS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    """ """
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=4)

def load_games():
    try:
        with open(GAMES_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_games(games):
    """ """
    with open(GAMES_FILE, 'w') as file:
        json.dump(games, file, indent=4)

def is_valid_email(email):
    """ """
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def sign_up(users):
    """ """
    print(Fore.CYAN + "\n=== Sign Up ===" + Style.RESET_ALL)
    
    username = input("Username: ").strip()
    email = input("Email: ").strip()
    password = input("Password (at least 8 characters): ").strip()

    if username in users:
        print(Fore.RED + "Username already exists. Please choose another." + Style.RESET_ALL)
        return

    if not is_valid_email(email):
        print(Fore.RED + "Invalid email format. Try again." + Style.RESET_ALL)
        return

    if any(user["email"] == email for user in users.values()):
        print(Fore.RED + "This email is already registered. Please use another." + Style.RESET_ALL)
        return

    if len(password) < 8:
        print(Fore.RED + "Password must be at least 8 characters." + Style.RESET_ALL)
        return

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user_id = str(uuid.uuid4())

    users[username] = {
        "id": user_id,
        "email": email,
        "password": hashed_password.decode('utf-8'),
        "score": 0
    }
    save_users(users)
    print(Fore.GREEN + "Sign-up successful!" + Style.RESET_ALL)

def log_in(users):
    """ """
    print(Fore.CYAN + "\n=== Log In ===" + Style.RESET_ALL)
    username = input("Username: ").strip()
    
    if username not in users:
        print(Fore.RED + "Username not found." + Style.RESET_ALL)
        return None

    password = input("Password: ").strip()
    hashed_password = users[username]["password"].encode('utf-8')

    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        print(Fore.GREEN + f"Welcome, {username}!" + Style.RESET_ALL)
        return username
    else:
        print(Fore.RED + "Incorrect password." + Style.RESET_ALL)
        return None

def start_new_game(users, games, current_user):
    """ """
    print(Fore.CYAN + "\n=== Start a New Game ===" + Style.RESET_ALL)
    opponent = input("Enter opponent's username: ").strip()

    if opponent not in users:
        print(Fore.RED + "Opponent's username not found." + Style.RESET_ALL)
        return

    password = input(f"Enter {opponent["name"]}'s password: ").strip()
    hashed_password = users[opponent]["password"].encode('utf-8')

    if not bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        print(Fore.RED + "Incorrect password for opponent." + Style.RESET_ALL)
        return

    game_id = str(uuid.uuid4())
    games[game_id] = {
        "players": [{"name": current_user,
                     "x": 8, 
                     "y": 0, 
                      "walls": 10
                      },
                    {"name": opponent,
                     "x": 8, 
                     "y": 16, 
                      "walls": 10
                      }],
        "state": "new", 
        "board": DEFAULT_BOARD,
        "turn": 0,
        "result": "unfinished"
    }
    save_games(games)
    print(Fore.GREEN + f"New game started! Game ID: {game_id}" + Style.RESET_ALL)
    game = games[game_id]
    print(game)
    input()
    save_games(games)
    quoridor2.playing(game_id, game["players"], None, game['turn'])


def continue_game(games, current_user):
    """ """
    print(Fore.CYAN + "\n=== Continue a Game ===" + Style.RESET_ALL)
    print(games)
    user_games = {gid: g for gid, g in games.items() if current_user in [x["name"] for x in g["players"]] and g["state"] != "finished"}
    
    if not user_games:
        print(Fore.RED + "No unfinished games found." + Style.RESET_ALL)
        return

    print(Fore.YELLOW + "Unfinished games:" + Style.RESET_ALL)
    for gid, game in user_games.items():
        print(f"Game ID: {gid}, Players: {game['players']}")

    game_id = input("Enter the Game ID to continue: ").strip()
    if game_id not in user_games:
        print(Fore.RED + "Invalid Game ID." + Style.RESET_ALL)
        return

    opponent = [p for p in user_games[game_id]["players"] if p != current_user][0]
    password = input(f"Enter {opponent["name"]}'s password: ").strip()
    hashed_password = load_users()[opponent]["password"].encode('utf-8')

    if not bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        print(Fore.RED + "Incorrect password for opponent." + Style.RESET_ALL)
        return

    print(Fore.GREEN + f"Continuing game {game_id}..." + Style.RESET_ALL)
    game = saving.load_game(game_id)
    print(game)
    quoridor2.playing(game_id, game["players"], game["board"], game['turn'])

def view_game_history(games, current_user):
    """ """
    print(Fore.CYAN + "\n=== Game History ===" + Style.RESET_ALL)
    user_games = {gid: g for gid, g in games.items() if current_user in g["players"]}

    if not user_games:
        print(Fore.RED + "No games found for this user." + Style.RESET_ALL)
        return

    print("Filter by state (new/in_progress/finished):")
    filter_state = input("Enter state or leave blank for all: ").strip()

    for gid, game in user_games.items():
        if not filter_state or game["state"] == filter_state:
            print(f"Game ID: {gid}, Players: {game['players']}, State: {game['state']}")

def view_leaderboard(users, games):
    """ """
    print(Fore.CYAN + "\n=== Leaderboard ===" + Style.RESET_ALL)
    leaderboard = {}

    for game in games.values():
        for player in game["players"]:
            if player not in leaderboard:
                leaderboard[player] = 0
            leaderboard[player] += 1

    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    print(Fore.YELLOW + "Player | Games Played" + Style.RESET_ALL)
    for player, games_played in sorted_leaderboard:
        print(f"{player} | {games_played}")

def main():
    users = load_users()
    games = load_games()

    current_user = None
    while True: 
        if not current_user:
            print(Fore.CYAN + "\n=== Main Menu ===" + Style.RESET_ALL)
            print(Fore.YELLOW + "1. Sign Up" + Style.RESET_ALL)
            print(Fore.GREEN + "2. Log In" + Style.RESET_ALL)
            print(Fore.RED + "3. Exit" + Style.RESET_ALL)

            choice = input("Choose an option: ").strip()
            if choice == '1':
                sign_up(users)
            elif choice == '2':
                current_user = log_in(users)
            elif choice == '3':
                print(Fore.GREEN + "Exiting the program. Goodbye!" + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "Invalid choice. Try again." + Style.RESET_ALL)
        else:
            print(Fore.CYAN + "\n=== User Menu ===" + Style.RESET_ALL)
            print(Fore.YELLOW + "1. Start a New Game" + Style.RESET_ALL)
            print(Fore.GREEN + "2. Continue Game" + Style.RESET_ALL)
            print(Fore.BLUE + "3. View Game History" + Style.RESET_ALL)
            print(Fore.MAGENTA + "4. View Leaderboard" + Style.RESET_ALL)
            print(Fore.RED + "5. Log Out" + Style.RESET_ALL)

            choice = input("Choose an option: ").strip()
            if choice == '1':
                start_new_game(users, games, current_user)
            elif choice == '2':
                continue_game(games, current_user)
            elif choice == '3':
                view_game_history(games, current_user)
            elif choice == '4':
                view_leaderboard(users, games)
            elif choice == '5':
                print(Fore.GREEN + f"Goodbye {current_user}!" + Style.RESET_ALL)
                current_user = None
            else:
                print(Fore.RED + "Invalid choice. Try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main()

import json #??

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