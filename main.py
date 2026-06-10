import random
import json

print("\n=== Anime/Game Recommendation App ===")

# ---------- HISTORY FUNCTIONS ----------

def save_history(text):
    with open("history.txt", "a") as file:
        file.write(text + "\n")

def read_history():
    """Read and display history from history.txt file"""
    try:
        with open("history.txt", "r") as file:
            data = file.read()
            if data.strip():
                print(data)
            else:
                print("No history found.")
    except FileNotFoundError:
        print("No history file found yet.")
    
def clear_history():
    with open("history.txt","w") as file:
        file.write("")
    
# ---------- GENRES ----------

anime_genres = {
    "1": "Action",
    "2": "Romance",
    "3": "Isekai",
    "4": "Horror"
}

game_genres = {
    "1": "Action",
    "2": "Pokemon",
    "3": "Open World",
    "4": "Horror"
}

# ---------- LOAD JSON DATA ----------

with open("anime_data.json","r") as anime_file:
    anime_data = json.load(anime_file)

with open("game_data.json","r") as game_file:
    game_data = json.load(game_file)

with open("fav_anime.json","r") as fav_anime:
    fav_anime_data = json.load(fav_anime)
    
with open("fav_game.json","r") as fav_game:
    fav_game_data = json.load(fav_game)

# ---------- SAVE JSON DATA ----------

def save_anime_data():
    """Save anime data to JSON file"""
    with open("anime_data.json", "w") as file:
        json.dump(anime_data, file, indent=4)

def save_game_data():
    """Save game data to JSON file"""
    with open("game_data.json", "w") as file:
        json.dump(game_data, file, indent=4)

def save_fav_anime():
    with open("fav_anime.json","w") as file:
        json.dump(fav_anime_data,file,indent = 4)
def save_fav_game():
    with open("fav_game.json","w") as file:
        json.dump(fav_game_data,file,indent = 4)

# ---------- SHOW FUNCTIONS ----------

def show_anime_genres():
    print("1. Action")
    print("2. Romance")
    print("3. Isekai")
    print("4. Horror")

def show_game_genres():
    print("1. Action")
    print("2. Pokemon")
    print("3. Open World")
    print("4. Horror")

def show_recom(items):
    if len(items) >= 3:
        random_items = random.sample(items, 3)
    else:
        random_items = items
    number = 1
    for item in random_items:
        print(f"✨ {number}. {item}")
        number += 1

def random_recom(items):
    if not items:
        print("No recommendations available.")
        return
    random_item = random.choice(items)
    print("\n=== Random Recommendation ===")
    print(random_item)
    save_history("Random Recommendation:")
    save_history(random_item)

# ---------- SEARCH FUNCTION ----------

def check_search(search, genre, category, data, key):
    if genre in search and category in search:
        show_recom(data[key])
        return True
    return False

# ---------- MAIN PROGRAM ----------

name = input("Enter your name: ")

print(f"\nWelcome, {name}, to the Anime/Game Recommendation App!")

while True:
    print("\n1. Anime")
    print("2. Game")
    print("3. View History")
    print("4. Add Anime")
    print("5. Add Game")
    print("6. Search")
    print("7. Clear History")
    print("8. Remove Anime")
    print("9. Remove Game")
    print("10. Add Favorit Anime")
    print("11. View Favorit Anime")
    print("12. Remove Favorit Anime")
    print("13. Add Favorit Game")
    print("14. View Favorit Game")
    print("15. Remove Favorit Game")
    print("16. Exit")

    menu_choice = input("\nSelect an option: ")

    # ---------- ANIME ----------

    if menu_choice == "1":
        save_history(f"{name} selected anime")
        show_anime_genres()
        choice = input("\nSelect your genre: ")
        if choice in anime_data:
            save_history(f"{name} selected {anime_genres[choice]} anime")
            print("\n=== Anime Recommendations ===")
            show_recom(anime_data[choice])
            random_recom(anime_data[choice])
        else:
            print("Invalid choice. Please try again.")

    # ---------- GAME ----------

    elif menu_choice == "2":
        save_history(f"{name} selected game")
        show_game_genres()
        choice = input("\nSelect your genre: ")
        if choice in game_data:
            save_history(f"{name} selected {game_genres[choice]} game")
            print("\n=== Game Recommendations ===")
            show_recom(game_data[choice])
            random_recom(game_data[choice])
        else:
            print("Invalid choice. Please try again.")

    # ---------- VIEW HISTORY ----------

    elif menu_choice == "3":
        print("\n=== Previous History ===")
        read_history()

    # ---------- ADD ANIME ----------

    elif menu_choice == "4":
        print("\n===Anime Genre===")
        show_anime_genres()
        choice_genre = input("\nSelect genre: ")
        if choice_genre in anime_data:
            new_anime = input("Enter anime name: ").title()
            if new_anime not in anime_data[choice_genre]:
                anime_data[choice_genre].append(new_anime)
            else:
                print("Anime already exists!")         
            save_anime_data()
            print(f"{new_anime} added successfully!")
            save_history(
                f"{name} added {new_anime} in {anime_genres[choice_genre]} anime"
            )
        else:
            print("Invalid choice.")

    # ---------- ADD GAME ----------

    elif menu_choice == "5":
        print("\n===Game Genre===")
        show_game_genres()
        choice_genre = input("\nSelect genre: ")
        if choice_genre in game_data:
            new_game = input("Enter game name: ").title()
            if new_game not in game_data[choice_genre]:
                game_data[choice_genre].append(new_game)
            else:
                print("Game already exists!")   
            save_game_data()
            print(f"{new_game} added successfully!")
            save_history(
                f"{name} added {new_game} in {game_genres[choice_genre]} game"
            )
        else:
            print("Invalid choice.")

    # ---------- SEARCH ----------

    elif menu_choice == "6":
        search = input("Search: ").lower()
        save_history(f"{name} searched: {search}")
        
        search_data = [
        # -------- anime section ---------
        ( "action", "anime", anime_data, "1"),
        ("romance", "anime", anime_data, "2"),
        ("isekai", "anime", anime_data, "3"),
        ("horror", "anime", anime_data, "4"),
        #-------- game section ---------
        ("action", "game", game_data, "1"),
        ("pokemon", "game", game_data, "2"),
        ("open world", "game", game_data, "3"),
        ("horror", "game", game_data, "4")
        ]
        found = False
        for genre, category, data, key in search_data:
            if check_search(search, genre, category, data, key):
                found = True
        if not found:
            print("No Result Found.")
                
    # ---------- CLEAR HISTORY ----------

    elif menu_choice == "7":
        clear_history()
        print("History cleared successfully!")
        
    # ---------- REMOVE ANIME ----------
    
    elif menu_choice == "8":
        show_anime_genres()
        choice_genre = input("Select anime genre: ")
        if choice_genre in anime_data:
            print("\n=== Anime List ===")
            for anime in anime_data[choice_genre]:
                print(anime)
            remove_anime = input(
            "\nEnter anime name to remove: "
        ).title()
            if remove_anime in anime_data[choice_genre]:
                    anime_data[choice_genre].remove(remove_anime)
                    save_anime_data()
                    print(f"{remove_anime} removed successfully!")
                    save_history(
                        f"{name} removed {remove_anime} in {anime_genres[choice_genre]}"
            )
            else:
                 print("Anime not found.")
        else:
            print("Invalid choice.")
    
    # ---------- REMOVE GAME ----------
  
    elif menu_choice == "9":
        show_game_genres()
        choice_genre = input("Select your genre: ")
        if choice_genre in game_data:
            print("===Game List===")
            for game in game_data[choice_genre]:
                print(game)
            remove_game = input("\nEnter game name to remove: ").title()
            if remove_game in game_data[choice_genre]:
                    game_data[choice_genre].remove(remove_game)
                    save_game_data()
                    print(f"{remove_game} removed successfully!")
                    save_history(
                     f"{name} removed {remove_game} in {game_genres[choice_genre]}"
                     )
            else:
                print("Game not found.")  
        else:
            print("Invalid choice.")
 
    # ---------- ADD FAVORIT ANIME ---------- 
  
    elif menu_choice == "10":
        fav_anime = input("Enter your favorite anime name: ").title() 
        if fav_anime not in fav_anime_data:
            fav_anime_data.append(fav_anime)
            save_fav_anime()
            print(f"{fav_anime} added successfully!")
            save_history(f"{name} added {fav_anime} in favorite anime.")
        else:
            print("Anime already exists in favorites!")
        
    # ---------- VIEW FAVORIT ANIME ----------
    
    elif menu_choice == "11":
        print("\n=== Favorite Anime ===")
        for anime in fav_anime_data:
            print(f"⭐ {anime}")   


    # --------- REMOVE FAVORIT ANIME ---------
    
    elif menu_choice == "12":
        if not fav_anime_data:
            print("No favorite anime found.")
        else:
            print("=== Favorite Anime List ===")
            for anime in fav_anime_data:
                print(anime)
            remove_anime = input("Select Anime Name: ").title()
            if remove_anime in fav_anime_data:
                fav_anime_data.remove(remove_anime)
                save_fav_anime()
                print(f"\n {remove_anime} removed successfully!")
                save_history(f"{name} removed {remove_anime} in favorite anime list.")
            else:
                print("Anime not found in favorite list.")

    # ---------- ADD FAVORITE GAME ----------   
    
    elif menu_choice == "13":
        fav_game = input("Enter your favorite game name: ").title()
        if fav_game not in fav_game_data:
            fav_game_data.append(fav_game)
            save_fav_game()
            print(f"{fav_game} added successfully!")
            save_history(f"{name} added {fav_game} in favorite game.")
        else:
            print("Game already exists in favorites!")
        
    # ---------- VIEW FAVORITE GAME ----------

    elif menu_choice == "14":
        print("\n=== Favorite Game ===")
        if not fav_game_data:
            print("No favorite Game found.")
        else:
            for game in fav_game_data:
                print(f"⭐ {game}")    
           
    # ---------- REMOVE FAVORIT GAME ----------
    
    elif menu_choice == "15":
        if not fav_game_data:
            print("No favorite game found.")
        else:
            print("=== Favorite Game List ===")
            for game in fav_game_data:
                print(game)
            remove_game = input("Select Game Name: ").title()
            if remove_game in fav_game_data:
                fav_game_data.remove(remove_game)
                save_fav_game()
                print(f"\n {remove_game} removed successfully!")
                save_history(f"{name} removed {remove_game} in favorite game list.")
            else:
                print("Game not found in favorite list.")
        
    # ---------- EXIT ----------

    elif menu_choice == "16":
        print(f"Goodbye, {name}!")
        break
    else:
        print("Invalid choice. Please try again.")

    print(f"\nThanks, {name}, for using the app!")