# Merged code: User management + Quoridor game logic

# User management functions (from import json.py)
import json
import re
import uuid
import bcrypt
from colorama import Fore, Style

def playing():
    #game board
    list = [["   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   ","|","   "] 
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

    #initial values
    list[0][8] = " 1 "
    list[16][8] = " 2 "
    x1p = 8
    y1p = 0
    x2p = 8
    y2p = 16
    nobat = 0
    Winner = ""
    s1 = 0
    s2 = 0
    wall1 = 0
    wall2 = 0
    wtf = ""




    #move up , down def
    def ud() :
        global yp
        global xp
        global y 
        global yw 
        global ys 
        global s1    
        if 0<=y<=16 and list[yw][int((xp/2))]!=" *  " :
            if list[y][xp]==f" {pll} " :
                if y == 0 or y == 16 :
                    a = input("Pleas choose between 'r' and 'l':")
                    if a=="r":
                        if (xp+2)<=16 :
                            list[yp][xp] = "   "
                            list[y][xp+2] = f" {pl} "
                            yp = y
                            xp = xp+2
                            return(yp , xp)
                        else :
                            print("This move is not allowed.")
                            s1 += 1
                            return(s1)
                    elif a=="l":
                        if (xp-2)>=0 :
                            list[yp][xp] = "   "
                            list[y][xp-2] = f" {pl} "
                            yp = y
                            xp = xp-2
                            return(yp , xp)
                        else:
                            print("This move is not allowed.")
                            s1 += 1
                            return(s1)
                    else:
                        print("This move is not allowed.")
                        s1 += 1
                        return(s1)  
                else :
                    if list[yws][int((x1p/2))]!=" *  " :
                        list[yp][xp] = "   "
                        list[ys][xp] = f" {pl} "
                        yp = ys
                        return(yp)
                    else :
                        a = input("Pleas choose between 'r' and 'l':")
                    if a=="r":
                        if (xp+2)<=16 :
                            list[yp][xp] = "   "
                            list[y][xp+2] = f" {pl} "
                            yp = y
                            xp = xp+2
                            return(yp , xp)
                        else :
                            print("This move is not allowed.")
                            s1 += 1
                            return(s1)
                    elif a=="l":
                        if (xp-2)>=0 :
                            list[yp][xp] = "   "
                            list[y][xp-2] = f" {pl} "
                            yp = y
                            xp = xp-2
                            return(yp , xp)
                        else:
                            print("This move is not allowed.")
                            s1 += 1
                            return(s1)
                    else:
                        print("This move is not allowed.")
                        s1 += 1
                        return(s1)
            else :
                list[yp][xp] = "   "
                list[y][xp] = f" {pl} "
                yp = y
                return(yp)
        else :
            print("This move is not allowed.")
            s1 += 1
            return(s1)

    #move right , left def
    def rl() :
        global yp
        global xp
        global x 
        global xw 
        global xs 
        global s1               
        if 0<=x<=16 and list[yp][xw]!="*" :
            if list[yp][x]==f" {pll} " :
                if x == 0 or x == 16 :
                    a = input("Pleas choose between 'u' and 'd':")
                    if a=="d":
                        if (yp+2)<=16 :
                            list[yp][xp] = "   "
                            list[yp+2][x] = f" {pl} "
                            yp = yp + 2
                            xp = x
                            return(yp , xp)
                        else :
                            print("This move is not allowed.")
                            s1 += 1
                            return(s1)
                    elif a=="u":
                        if (yp-2)>=0 :
                            list[yp][xp] = "   "
                            list[yp-2][x] = f" {pl} "
                            yp = yp + 2
                            xp = x
                            return(yp , xp)
                        else:
                            print("This move is not allowed.")
                            s1 += 1
                            return(s1)
                    else:
                        print("This move is not allowed.") 
                        s1 += 1
                        return(s1)    
                else :
                    if list[yp][xws]!="*" :
                        list[yp][xp] = "   "
                        list[yp][xs] = f" {pl} "
                        xp = xs
                        return(xp)
                    else :
                        a = input("Pleas choose between 'r' and 'l':")
                        if a=="d":
                            if (yp+2)<=16 :
                                list[yp][xp] = "   "
                                list[yp+2][x] = f" {pl} "
                                yp = yp + 2
                                xp = x
                                return(yp , xp)
                            else :
                                print("This move is not allowed.")
                                s1 += 1
                                return(s1)
                        elif a=="u":
                            if (yp-2)>=0 :
                                list[yp][xp] = "   "
                                list[yp-2][x] = f" {pl} "
                                yp = yp + 2
                                xp = x
                                return(yp , xp)
                            else:
                                print("This move is not allowed.")
                                s1 += 1
                                return(s1)
                        else:
                            print("This move is not allowed.") 
                            s1 += 1
                            return(s1)    
            else :
                list[yp][xp] = "   "
                list[yp][x] = f" {pl} "
                xp = x
                return(xp)
        else :
            print("This move is not allowed.")
            s1 += 1
            return(s1)


    #let's play
    while 1 :
            #game board
            for i in list :
                    print("".join(i))
            #who won ?
            if y1p == 16 :
                print("Player 1 won.")
                break
            if y2p == 0 :
                print("Player 2 won.")
                break
            #player 1
            if nobat%2 == 0 :
                    print("Player number 1's turn :")
                    print("Pleas choose between 'd' , 'u' , 'r' , 'l' and 'wall'.")
                    pl = "1"
                    pll = "2"
                    yp = y1p
                    xp = x1p
                    mw = input()
                    if mw == "exit" :
                            break
                    elif mw == "d" :
                        y = yp + 2
                        yw = yp + 1
                        ys = yp + 4
                        yws = yp + 3
                        ud()
                        if s1 == s2 :
                            y1p = yp
                            x1p = xp
                            nobat +=1
                        else :
                            s2 += 1
                            continue    
                    elif mw == "u" :
                        y = yp - 2
                        yw = yp - 1
                        ys = yp - 4
                        yws = yp - 3
                        ud()
                        if s1 == s2 :
                            y1p = yp
                            x1p = xp
                            nobat +=1
                        else :
                            s2 += 1
                            continue    
                    elif mw == "r" :
                        x = xp +2
                        xw = xp + 1
                        xs = xp + 4
                        xws = xp + 3
                        rl()
                        if s1 == s2 :
                            y1p = yp
                            x1p = xp
                            nobat +=1  
                        else :
                            s2 += 1
                            continue
                    elif mw == "l" :
                        x = xp - 2
                        xw = xp - 1
                        xs = xp - 4
                        xws = xp - 3
                        rl()
                        if s1 == s2 :
                            y1p = yp
                            x1p = xp
                            nobat +=1
                        else :
                            s2 += 1
                            continue
            # wall player 1         
                    elif mw == "wall" :
                        wallleft = 10-wall1
                        print(f"you have {wallleft} walls left.")
                        if wall1 < 10 :
                            wall()
                            if wtf == "t" :
                                wall1 += 1
                                nobat += 1
                        else :
                            print("you are out of walls.")
                    else :
                            print("Pleas choose between 'd' , 'u' , 'r' , 'l' and 'wall'.")
                            
            #player 2
            else :
                    print("Player number 2's turn :")
                    print("Pleas choose between 'd' , 'u' , 'r' , 'l' and 'wall'.")
                    pl = "2"
                    pll = "1"
                    yp = y2p
                    xp = x2p
                    mw = input()
                    if mw == "exit" :
                            break
                    elif mw == "d" :
                        y = yp + 2
                        yw = yp + 1
                        ys = yp + 4
                        yws = yp + 3
                        ud()
                        if s1 == s2 :
                            y2p = yp
                            x2p = xp
                            nobat +=1
                        else :
                            s2 += 1
                            continue     
                    elif mw == "u" :
                        y = yp - 2
                        yw = yp - 1
                        ys = yp - 4
                        yws = yp - 3
                        ud()
                        if s1 == s2 :
                            y2p = yp
                            x2p = xp
                            nobat +=1 
                        else:
                            s2 += 1
                            continue       
                    elif mw == "r" :
                        x = xp +2
                        xw = xp + 1
                        xs = xp + 4
                        xws = xp + 3
                        rl()
                        if s1 == s2 :
                            y2p = yp
                            x2p = xp
                            nobat +=1
                        else :
                            s2 += 1
                            continue    
                    elif mw == "l" :
                        x = xp - 2
                        xw = xp - 1
                        xs = xp - 4
                        xws = xp - 3
                        rl()
                        if s1 == s2 :
                            y2p = yp
                            x2p = xp
                            nobat +=1
                        else:
                            s2 += 1
                            continue
            # wall player 2 
                    elif mw == "wall" :
                        wallleft = 10-wall2
                        print(f"you have {wallleft} walls left.")
                        if wall2 < 10 :
                            wall()
                            if wtf == "t" :
                                wall2 += 1
                                nobat += 1
                        else :
                            print("you are out of walls.")
                    else :
                            print("Pleas choose between 'd' , 'u' , 'r' , 'l' and 'wall'.")

USERS_FILE = "users.json"
GAMES_FILE = "games.json"

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

    password = input(f"Enter {opponent}'s password: ").strip()
    hashed_password = users[opponent]["password"].encode('utf-8')

    if not bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        print(Fore.RED + "Incorrect password for opponent." + Style.RESET_ALL)
        return

    game_id = str(uuid.uuid4())
    games[game_id] = {
        "players": [current_user, opponent],
        "state": "new"
    }
    save_games(games)
    print(Fore.GREEN + f"New game started! Game ID: {game_id}" + Style.RESET_ALL)
    playing()


def continue_game(games, current_user):
    """ """
    print(Fore.CYAN + "\n=== Continue a Game ===" + Style.RESET_ALL)
    user_games = {gid: g for gid, g in games.items() if current_user in g["players"] and g["state"] != "finished"}

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
    password = input(f"Enter {opponent}'s password: ").strip()
    hashed_password = load_users()[opponent]["password"].encode('utf-8')

    if not bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        print(Fore.RED + "Incorrect password for opponent." + Style.RESET_ALL)
        return

    print(Fore.GREEN + f"Continuing game {game_id}..." + Style.RESET_ALL)

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

# Quoridor game logic (from quoridor2.py)
def start_quoridor_game(current_user):
    print(f"Starting the Quoridor game for user: {current_user}")
    # Original Quoridor game logic starts here

if __name__ == "__main__":
    users = load_users()
    current_user = None

    # User authentication before starting the game
    while True:
        print("\n=== Welcome to Quoridor ===")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            sign_up(users)
        elif choice == '2':
            current_user = log_in(users)
            if current_user:
                break  # Exit the loop and start the game
        elif choice == '3':
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

    # Start the Quoridor game after successful authentication
    print(f"Hello {current_user}, welcome to Quoridor!")
    start_quoridor_game(current_user)
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
if __name__ == "__main__":
    record_game()

save_game_data
python
Copy
Edit
def save_game_data(game_data, file_path):
    """Save game data to a JSON file."""


game_data: 
file_path: 

python
Copy
Edit
    try:
        with open(file_path, 'r') as file:
            games = json.load(file)
    except FileNotFoundError:
        games = []

python
Copy
Edit
    games.append(game_data)

python
Copy
Edit
    with open(file_path, 'w') as file:
        json.dump(games, file, indent=4)

python
Copy
Edit
def record_game():
    """Record a new game's data."""

python
Copy
Edit
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



if __name__ == "__main__":
    record_game()


