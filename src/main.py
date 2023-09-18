"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503
"""

import json
import os
import sys

import requests


from YuGiOh.Deck import Deck
from Archetypes.DD import dd_combos as combos_dd

URL: str = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
# ITERATIONS: int = 1
ITERATIONS: int = 10_000


def get_local_database() -> dict:
    local_database: dict = {}
    path_to_local_database: str = "../assets/database.json"
    if os.path.exists(path_to_local_database):
        with open(path_to_local_database, "r") as file:
            local_database: dict = json.load(file)
            pass
        pass
    return local_database


def create_deck(path_to_deck: str, local_database: dict) -> Deck:
    deck: Deck = Deck()
    with open(path_to_deck, "r") as file:
        deck_type: str = ""
        local_database_updated: bool = False
        for line in file:
            line: str = line.strip()
            if line.startswith("!"):
                break
                pass
            if len(line.split(" ")) < 2:
                if line.startswith("#"):
                    deck_type: str = line[1:]
                    pass
                else:
                    card_id: str = line
                    if card_id not in local_database:
                        request: request = requests.get(f"{URL}?id={card_id}")
                        local_database[card_id] = request.json()["data"][0]
                        local_database_updated: bool = True
                        pass
                    card_name: str = local_database[card_id]["name"]
                    if deck_type == "main":
                        deck.add_card_to_main_deck(card_name)
                        pass
                    else:
                        deck.add_card_to_extra_deck(card_name)
                        pass
                    pass
                pass
            pass
        pass
    if local_database_updated:
        with open("../assets/database.json", "w") as file:
            json.dump(local_database, file)
            pass
        pass
    return deck


def main() -> None:
    # print(sys.argv)
    # Terminates the program if the user has not provided any arguments
    if len(sys.argv) < 2:
        sys.exit("User failed to provide a deck...\n"
                 "Terminating Program.")
        pass
    # Terminates the program if the user has not given a deck to analyze
    if not sys.argv[1].endswith(".ydk"):
        sys.exit("File extension error...\n"
                 "A valid deck must end with the file extension '.ydk'...\n"
                 "Terminating Program.")
        pass
    deck_name: str = sys.argv[1]
    path_to_deck: str = f"../assets/decks/{deck_name}"
    # Terminates the program if the deck to analyze does not exist
    if not (os.path.exists(path_to_deck)):
        sys.exit(f"Deck '{deck_name}' does not exist...\n"
                 f"Please place the deck in the 'assets/decks' directory.")
        pass
    # Get the local database
    local_database: dict = get_local_database()
    # Create a deck
    deck = create_deck(path_to_deck, local_database)
    combos_dd.add_all_combos(deck, local_database)
    deck.analyze(ITERATIONS, local_database)
    deck.print_analysis(ITERATIONS, analysis_level=3)
    return None


if __name__ == '__main__':
    main()
    pass
