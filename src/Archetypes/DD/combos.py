"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503
"""
from src.YuGiOh.ComboCategory import ComboCategory
from src.YuGiOh.Deck import Deck
from src.Archetypes.DD.tournament_combos import one_card_combos


def anime_combos(deck: Deck, local_database: dict) -> None:
    # kings_combos(deck, local_database)
    # emperors_combos(deck, local_database)
    # super_doom_combos(deck, local_database)
    return None


def tournament_combos() -> ComboCategory:
    all_tournament_combos: ComboCategory = ComboCategory("Tournament Combos")
    all_tournament_combos.add_combo(one_card_combos.all_one_card_combos())
    return all_tournament_combos


def add_all_combos(deck: Deck) -> None:
    # deck.add_combo_category(anime_combos())
    deck.add_combo_category(tournament_combos())
    return None
