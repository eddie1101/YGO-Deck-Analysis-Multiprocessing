"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503
"""


def get_card_data(card_name: str, local_database: dict) -> dict:
    for value in local_database.values():
        if value["name"] == card_name:
            return value
        pass
    return {}


def card_is_main_deck_pendulum(card_data) -> bool:
    flag_1: bool = card_data["frameType"] == "normal_pendulum"
    flag_2: bool = card_data["frameType"] == "effect_pendulum"
    flag_3: bool = card_data["frameType"] == "ritual_pendulum"
    return flag_1 or flag_2 or flag_3


def find_card_by_scales(source: list, local_database: dict, low: int,
                        high: int, scale_a: str = "",
                        scale_b: str = "") -> str | None:
    for card in source:
        card_data: dict = get_card_data(card, local_database)
        if card_is_main_deck_pendulum(card_data):
            if low <= card_data["scale"] <= high:
                if scale_a != "":
                    if scale_a != card_data["name"]:
                        return card_data["name"]
                    pass
                else:
                    if scale_b != card_data["name"]:
                        return card_data["name"]
                    pass
                pass
            pass
        pass
    return None


def normal_summon(card: str, hand: list) -> bool:
    if card in hand:
        hand.remove(card)
        return True
    return False


def special_summon_from_hand(monster: str, hand: list) -> bool:
    if monster in hand:
        hand.remove(monster)
        return True
    return False


def special_summon_from_deck(monster: str, main_deck: list) -> bool:
    if monster in main_deck:
        main_deck.remove(monster)
        return True
    return False


def add_card_from_deck_to_hand(card: str, hand: list, main_deck: list) -> bool:
    if card in main_deck:
        hand.append(card)
        main_deck.remove(card)
        return True
    return False


# def add_card_from_GY_to_hand(card: str, hand: list, graveyard: list) -> bool:
#     if card in graveyard:
#         hand.append(card)
#         graveyard.remove(card)
#         return True
#     return False


def dump_card_from_deck_to_GY(card: str, main_deck: list) -> bool:
    if card in main_deck:
        # graveyard.append(card)
        main_deck.remove(card)
        return True
    return False


def discard_card(card: str, hand: list) -> bool:
    if card in hand:
        hand.remove(card)
        return True
    return False


def extra_deck_summon(monster: str, extra_deck: list) -> bool:
    if monster in extra_deck:
        extra_deck.remove(monster)
        return True
    return False


def soft_brick_in_hand(card: str, hand: list) -> bool:
    return card in hand


def activate_spell_from_hand(card: str, hand: list) -> bool:
    if card in hand:
        hand.remove(card)
        return True
    return False


def set_scales(scales: tuple, hand: list, main_deck: list) -> None:
    scale_a, scale_b = scales
    if (scale_a in main_deck) and (scale_b in main_deck):
        main_deck.remove(scale_a)
        main_deck.remove(scale_b)
        pass
    else:
        hand.remove(scale_a)
        hand.remove(scale_b)
        pass
    return None
