"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503
"""

from src.YuGiOh import utils


def kepler_search(card: str, hand: list, main_deck: list) -> bool:
    return utils.add_card_from_deck_to_hand(card, hand, main_deck)


def gate_search(card: str, hand: list, main_deck: list) -> bool:
    return utils.add_card_from_deck_to_hand(card, hand, main_deck)


def gryphon_search(card: str, hand: list, main_deck: list) -> bool:
    return utils.add_card_from_deck_to_hand(card, hand, main_deck)


def gryphon_special_summon(card: str, hand: list) -> bool:
    return utils.special_summon_from_hand(card, hand)


def caesar_search(card: str, hand: list, main_deck: list) -> bool:
    return utils.add_card_from_deck_to_hand(card, hand, main_deck)


def swirl_fuse(fusion_card: str, material: str, hand: list,
               extra_deck: list) -> bool:
    if (material in hand) and (fusion_card in extra_deck):
        hand.remove("D/D Swirl Slime")
        hand.remove(material)
        extra_deck.remove(fusion_card)
        return True
    return False


def swirl_special_summon(target: str, hand: list) -> bool:
    return utils.special_summon_from_hand(target, hand)


def copernicus_dump(card: str, main_deck: list) -> bool:
    return utils.dump_card_from_deck_to_GY(card, main_deck)


# def copernicus_dump(card: str, main_deck: list, graveyard: list) -> bool:
#     return utils.dump_card_from_deck_to_GY(card, main_deck, graveyard)


def tell_dump(card: str, main_deck: list) -> bool:
    return utils.dump_card_from_deck_to_GY(card, main_deck)


# def tell_dump(card: str, main_deck: list, graveyard: list) -> bool:
#     return utils.dump_card_from_deck_to_GY(card, main_deck, graveyard)


def gilgamesh_scales(hand: list, main_deck: list, local_database: dict,
                     a_name: str = "", a_low: int = 0, a_high: int = 13,
                     b_name: str = "", b_low: int = 0,
                     b_high: int = 13) -> tuple | None:
    if (a_name != "") and (b_name != ""):
        if (a_name in main_deck) and (b_name in main_deck):
            return a_name, b_name
        elif (a_name in hand) and (b_name in hand):
            return a_name, b_name
        pass
    elif a_name != "":
        if a_name in main_deck:
            card_b_name: str | None = utils.find_card_by_scales(main_deck,
                                                                local_database,
                                                                b_low, b_high,
                                                                scale_a=a_name)
            if card_b_name is not None:
                return a_name, card_b_name
            pass
        else:
            card_b_name: str | None = utils.find_card_by_scales(hand,
                                                                local_database,
                                                                b_low, b_high,
                                                                scale_a=a_name)
            if card_b_name is not None:
                return a_name, card_b_name
            pass
        pass
    elif b_name != "":
        if b_name in main_deck:
            card_a_name: str | None = utils.find_card_by_scales(main_deck,
                                                                local_database,
                                                                a_low, a_high,
                                                                scale_b=b_name)
            if card_a_name is not None:
                return card_a_name, b_name
            pass
        else:
            card_a_name: str | None = utils.find_card_by_scales(hand,
                                                                local_database,
                                                                a_low, a_high,
                                                                scale_b=b_name)
            if card_a_name is not None:
                return card_a_name, b_name
            pass
        pass
    else:
        card_a_name: str | None = utils.find_card_by_scales(main_deck,
                                                            local_database,
                                                            a_low,
                                                            a_high)
        if card_a_name is not None:
            card_b_name: str | None = utils.find_card_by_scales(main_deck,
                                                                local_database,
                                                                b_low,
                                                                b_high,
                                                                scale_a=card_a_name)
            if card_b_name is not None:
                return card_a_name, card_b_name
            pass
        card_a_name: str | None = utils.find_card_by_scales(hand,
                                                            local_database,
                                                            a_low,
                                                            a_high)
        if card_a_name is not None:
            card_b_name: str | None = utils.find_card_by_scales(hand,
                                                                local_database,
                                                                b_low,
                                                                b_high,
                                                                scale_a=card_a_name)
            if card_b_name is not None:
                return card_a_name, card_b_name
            pass
        pass
    return None


def thomas_summon(main_deck: list, local_database: dict,
                  card_name: str = "") -> str | bool:
    for card in main_deck:
        card_data: dict = utils.get_card_data(card, local_database)
        cond_1: bool = "Monster" in card_data["type"]
        cond_2: bool = card_data["level"] == 8
        cond_3: bool = card_data["name"] != "D/D Savant Thomas"
        if all([cond_1, cond_2, cond_3]):
            cond_4: bool = card_name == ""
            cond_5: bool = card_name == card_data["name"]
            if any([cond_4, cond_5]):
                card_name: str = card_data["name"]
                main_deck.remove(card_name)
                return True
            pass
        pass
    return False
