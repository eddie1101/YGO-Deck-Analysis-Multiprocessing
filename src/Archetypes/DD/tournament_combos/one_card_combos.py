"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503
"""

from src.Archetypes.DD import utils as utils_dd
from src.YuGiOh import utils
from src.YuGiOh.Combo import Combo
from src.YuGiOh.ComboLine import ComboLine


def line_1(hand: list, main_deck: list, extra_deck: list,
           local_database: dict) -> bool:
    """
    Starting Hand:
        1. D/D Savant Kepler

    Searched Cards:
        2. Dark Contract with the Gate
        3. D/D Gryphon
        5. Scales (0 Scale + D/D Cerberus)
        13. Dark Contract with the Swamp King

    Dumped Cards:
        9. D/D Necro Slime

    Extra Deck Monsters:
        4. D/D/D Abyss King Gilgamesh
        6. D/D/D Wave King Caesar
        7. D/D/D Marksman King Tell
        8. D/D/D Abyss King Gilgamesh
        10. D/D/D Flame King Genghis
        11. D/D/D Deviser King Deus Machinex
        12. D/D/D Abyss King Gilgamesh
        14. D/D/D Flame King Genghis
        15. D/D/D Wave High King Caesar
        16. D/D/D Deviser King Deus Machinex

    Combo Line:
        1. NS Kepler; Add Gate
        2. Activate Gate; Add Gryphon
        3. Gryphon ME (Hand); SS itself
        4. LS Gilgamesh [Kepler + Gryphon]; Scale (0 Scale + Cerberus)
        5. PS Kepler and Gryphon
        6. Cerberus PE; Change Kepler's lv to 4
        7. XS R4 Caesar [Kepler + Gryphon]
        8. XS R5 Tell [Caesar]
        9. Tell eff; Burn for 1k
        10. LS Gilgamesh [Tell + Gilgamesh]
        11. Tell eff (GY); Dump Necro Slime
        12. Necro eff (GY); FS Genghis [Necro + Gilgamesh]
        13. XS R10 Machinex [Gilgamesh]
        14. Genghis eff; Revive Caesar
        15. LS Gilgamesh [Caesar + Machinex]
        16. Caesar eff (GY); Add Swamp King
        17. Activate Swamp King; FS Genghis [Genghis (GY) + Gilgamesh (GY)]
        18. XS R6 High Caesar [Genghis + Genghis]
        19. XS R10 Machinex [Gilgamesh]
    """
    hand_1: str = "D/D Savant Kepler"
    utils.normal_summon(hand_1, hand)
    card: str = "Dark Contract with the Gate"
    if not utils_dd.kepler_search(card, hand, main_deck):
        if not utils.soft_brick_in_hand(card, hand):
            return False
        pass
    utils.activate_spell_from_hand(card, hand)
    card: str = "D/D Gryphon"
    if not utils_dd.gate_search(card, hand, main_deck):
        if not utils.soft_brick_in_hand(card, hand):
            return False
        pass
    utils_dd.gryphon_special_summon(card, hand)
    card: str = "D/D/D Abyss King Gilgamesh"
    if not utils.extra_deck_summon(card, extra_deck):
        return False
    scale_a_val: int = 0
    scale_b_name: str = "D/D Cerberus"
    scales: tuple | None = utils_dd.gilgamesh_scales(hand, main_deck,
                                                     local_database,
                                                     a_high=scale_a_val,
                                                     b_name=scale_b_name)
    if scales is None:
        return False
    utils.set_scales(scales, hand, main_deck)
    cards: list = [
        "D/D/D Wave King Caesar",
        "D/D/D Marksman King Tell",
        "D/D/D Abyss King Gilgamesh"
    ]
    for card in cards:
        if not utils.extra_deck_summon(card, extra_deck):
            return False
        pass
    card: str = "D/D Necro Slime"
    if not utils.dump_card_from_deck_to_GY(card, main_deck):
        if not utils.soft_brick_in_hand(card, hand):
            return False
        else:
            utils.discard_card(card, hand)
            pass
        pass
    cards: list = [
        "D/D/D Flame King Genghis",
        "D/D/D Deviser King Deus Machinex",
        "D/D/D Abyss King Gilgamesh"
    ]
    for card in cards:
        if not utils.extra_deck_summon(card, extra_deck):
            return False
        pass
    card: str = "Dark Contract with the Swamp King"
    if not utils.dump_card_from_deck_to_GY(card, main_deck):
        if not utils.soft_brick_in_hand(card, hand):
            return False
        pass
    utils.activate_spell_from_hand(card, hand)
    cards: list = [
        "D/D/D Flame King Genghis",
        "D/D/D Wave High King Caesar",
        "D/D/D Deviser King Deus Machinex"
    ]
    for card in cards:
        if not utils.extra_deck_summon(card, extra_deck):
            return False
        pass
    return True


def line_2(hand: list, main_deck: list, extra_deck: list,
           local_database: dict) -> bool:
    """
    Starting Hand:
        1. D/D Savant Kepler

    Searched Cards:
        2. Dark Contract with the Gate
        3. D/D Gryphon
        5. Scales [0 Scale + D/D Cerberus]
        8. Dark Contract with the Swamp King
        11. D/D/D Headhunt

    Extra Deck Monsters:
        4. D/D/D Abyss King Gilgamesh
        6. D/D/D Wave King Caesar
        7. D/D/D Abyss King Gilgamesh
        9. D/D/D Flame King Genghis
        10. D/D/D Deviser King Deus Machinex
        12. D/D/D Abyss King Gilgamesh

    Combo Line:
        1. NS Kepler; Add Gate
        2. Activate Gate; Add Gryphon
        3. Gryphon ME (Hand); SS itself
        4. LS Gilgamesh [Kepler + Gryphon]; Scale (0 Scale + Cerberus)
        5. PS Kepler and Gryphon
        6. Cerberus PE; Change Kepler's lv to 4
        7. XS R4 Caesar [Kepler + Gryphon]
        8. LS Gilgamesh [Caesar + Gilgamesh]
        9. Caesar eff (GY); Add Swamp King
        10. Activate Swamp King; FS Genghis [Kepler (GY) + Gilgamesh (GY)]
        11. XS R10 Machinex [Gilgamesh]
        12. Genghis eff; Reborn Gryphon
        13. Gryphon ME; Add Headhunt
        14. LS Gilgamesh [Gryphon + Genghis]
        15. Set Headhunt
    """
    hand_1: str = "D/D Savant Kepler"
    utils.normal_summon(hand_1, hand)
    card: str = "Dark Contract with the Gate"
    if not utils_dd.kepler_search(card, hand, main_deck):
        if not utils.soft_brick_in_hand(card, hand):
            return False
        pass
    utils.activate_spell_from_hand(card, hand)
    card: str = "D/D Gryphon"
    if not utils_dd.gate_search(card, hand, main_deck):
        if not utils.soft_brick_in_hand(card, hand):
            return False
        pass
    utils_dd.gryphon_special_summon(card, hand)
    card: str = "D/D/D Abyss King Gilgamesh"
    if not utils.extra_deck_summon(card, extra_deck):
        return False
    scale_a_val: int = 0
    scale_b_name: str = "D/D Cerberus"
    scales: tuple | None = utils_dd.gilgamesh_scales(hand, main_deck,
                                                     local_database,
                                                     a_high=scale_a_val,
                                                     b_name=scale_b_name)
    if scales is None:
        return False
    utils.set_scales(scales, hand, main_deck)
    cards: list = [
        "D/D/D Wave King Caesar",
        "D/D/D Abyss King Gilgamesh"
    ]
    for card in cards:
        if not utils.extra_deck_summon(card, extra_deck):
            return False
        pass
    card: str = "Dark Contract with the Swamp King"
    if not utils_dd.caesar_search(card, hand, main_deck):
        if not utils.soft_brick_in_hand(card, hand):
            return False
        pass
    utils.activate_spell_from_hand(card, hand)
    cards: list = [
        "D/D/D Flame King Genghis",
        "D/D/D Deviser King Deus Machinex"
    ]
    for card in cards:
        if not utils.extra_deck_summon(card, extra_deck):
            return False
        pass
    card: str = "D/D/D Headhunt"
    if not utils_dd.gryphon_search(card, hand, main_deck):
        if utils.soft_brick_in_hand(card, hand):
            return False
        pass
    card: str = "D/D/D Abyss King Gilgamesh"
    if not utils.extra_deck_summon(card, extra_deck):
        return False
    return True


def line_3(hand: list, main_deck: list, extra_deck: list,
           local_database: dict) -> bool:
    """
    Starting Hand:
        1. D/D Savant Kepler

    Searched Cards:
        2. Dark Contract with the Gate
        3. D/D Gryphon
        5. Scales [0 Scale + D/D Cerberus]
        8. Dark Contract with the Swamp King
        11. D/D/D Headhunt

    Extra Deck Monsters:
        4. D/D/D Abyss King Gilgamesh
        6. D/D/D Wave King Caesar
        7. D/D/D Abyss King Gilgamesh
        9. D/D/D Flame King Genghis
        10. D/D/D Deviser King Deus Machinex

    Combo Line:
        1. NS Kepler; Add Gate
        2. Activate Gate; Add Gryphon
        3. Gryphon ME (Hand); SS itself
        4. LS Gilgamesh [Kepler + Gryphon]; Scale (0 Scale + Cerberus)
        5. PS Kepler and Gryphon
        6. Cerberus PE; Change Kepler's lv to 4
        7. XS R4 Caesar [Kepler + Gryphon]
        8. LS Gilgamesh [Caesar + Gilgamesh]
        9. Caesar eff (GY); Add Swamp King
        10. Activate Swamp King; FS Genghis [Kepler (GY) + Gilgamesh (GY)]
        11. XS R10 Machinex [Gilgamesh]
        12. Genghis eff; Reborn Gryphon
        13. Gryphon ME; Add Headhunt
        14. Set Headhunt
    """
    hand_1: str = "D/D Savant Kepler"
    utils.normal_summon(hand_1, hand)
    card: str = "Dark Contract with the Gate"
    if not utils_dd.kepler_search(card, hand, main_deck):
        if not utils.soft_brick_in_hand(card, hand):
            return False
        pass
    utils.activate_spell_from_hand(card, hand)
    card: str = "D/D Gryphon"
    if not utils_dd.gate_search(card, hand, main_deck):
        if not utils.soft_brick_in_hand(card, hand):
            return False
        pass
    utils_dd.gryphon_special_summon(card, hand)
    card: str = "D/D/D Abyss King Gilgamesh"
    if not utils.extra_deck_summon(card, extra_deck):
        return False
    scale_a_val: int = 0
    scale_b_name: str = "D/D Cerberus"
    scales: tuple | None = utils_dd.gilgamesh_scales(hand, main_deck,
                                                     local_database,
                                                     a_high=scale_a_val,
                                                     b_name=scale_b_name)
    if scales is None:
        return False
    utils.set_scales(scales, hand, main_deck)
    cards: list = [
        "D/D/D Wave King Caesar",
        "D/D/D Abyss King Gilgamesh"
    ]
    for card in cards:
        if not utils.extra_deck_summon(card, extra_deck):
            return False
        pass
    card: str = "Dark Contract with the Swamp King"
    if not utils_dd.caesar_search(card, hand, main_deck):
        if not utils.soft_brick_in_hand(card, hand):
            return False
        pass
    utils.activate_spell_from_hand(card, hand)
    cards: list = [
        "D/D/D Flame King Genghis",
        "D/D/D Deviser King Deus Machinex"
    ]
    for card in cards:
        if not utils.extra_deck_summon(card, extra_deck):
            return False
        pass
    card: str = "D/D/D Headhunt"
    if not utils_dd.gryphon_search(card, hand, main_deck):
        if utils.soft_brick_in_hand(card, hand):
            return False
        pass
    return True


def line_4(hand: list, main_deck: list, extra_deck: list,
           local_database: dict) -> bool:
    """
    Starting Hand:
        1. D/D Savant Kepler

    Searched Cards:
        2. Dark Contract with the Gate
        3. D/D Gryphon
        5. Scales [D/D Orthros + D/D Savant Thomas]
        6. Lv 8 DDD

    Extra Deck Monsters:
        4. D/D/D Abyss King Gilgamesh
        7. D/D/D Duo-Dawn King Kali Yuga
        8. D/D/D Deviser King Deus Machinex

    Combo Line:
        1. NS Kepler; Add Gate
        2. Activate Gate; Add Gryphon
        3. Gryphon ME (Hand); SS itself
        4. LS Gilgamesh [Kepler + Gryphon]; Scale (Orthros + Thomas)
        5. Thomas PE; Add Kepler
        6. Orthros PE; Pop Thomas and Gilgamesh
        7. Scale Kepler
        8. PS Thomas
        9. Thomas eff; Pop Kepler to SS Lv 8 DDD
        10. XS R8 Kali Yuga [Thomas + Lv8 DDD]
        11. XS R10 Machinex [Kali Yuga]
    """
    hand_1: str = "D/D Savant Kepler"
    utils.normal_summon(hand_1, hand)
    card: str = "Dark Contract with the Gate"
    if not utils_dd.kepler_search(card, hand, main_deck):
        if not utils.soft_brick_in_hand(card, hand):
            return False
        pass
    utils.activate_spell_from_hand(card, hand)
    card: str = "D/D Gryphon"
    if not utils_dd.gate_search(card, hand, main_deck):
        if not utils.soft_brick_in_hand(card, hand):
            return False
        pass
    utils_dd.gryphon_special_summon(card, hand)
    card: str = "D/D/D Abyss King Gilgamesh"
    if not utils.extra_deck_summon(card, extra_deck):
        return False
    scale_a_name: str = "D/D Orthros"
    scale_b_name: str = "D/D Savant Thomas"
    scales: tuple | None = utils_dd.gilgamesh_scales(hand, main_deck,
                                                     local_database,
                                                     a_name=scale_a_name,
                                                     b_name=scale_b_name)
    if scales is None:
        return False
    utils.set_scales(scales, hand, main_deck)
    thomas_target: str | None = utils_dd.thomas_summon(main_deck,
                                                       local_database)
    if thomas_target is None:
        return False
    cards: list = [
        "D/D/D Duo-Dawn King Kali Yuga",
        "D/D/D Deviser King Deus Machinex"
    ]
    for card in cards:
        if not utils.extra_deck_summon(card, extra_deck):
            return False
        pass
    return True


def line_X(hand: list, main_deck: list, extra_deck: list,
           local_database: dict) -> bool:
    """
    Starting Hand:
        x.

    Searched Cards:
        x.

    Dumped Cards:
        x.

    Extra Deck Monsters:
        x.

    Combo Line:
        1.

    LINE 1 (Gilgamesh gains Requiem eff):
    Normal Kepler add Gate, Gate search Vice Requiem
    Scale Requiem, Requiem effect targeting Gate
    Requiem + Kepler -> Gilgamesh, scale any scale no higher than 6 and Thomas
    Thomas effect add Kepler
    Gilgamesh effect destroy Thomas & return a contract
    Scale Kepler, Pendulum Thomas & Requiem
    XYZ / Requiem + Thomas -> Kali Yuga
    """
    return True


def line_X(hand: list, main_deck: list, extra_deck: list,
           local_database: dict) -> bool:
    """
    Starting Hand:
        x.

    Searched Cards:
        x.

    Dumped Cards:
        x.

    Extra Deck Monsters:
        x.

    Combo Line:
        1.

    LINE 1 (Gilgamesh gains Requiem eff):
    Normal Kepler add Gate, Gate search Vice Requiem
    Scale Requiem, Requiem effect targeting Gate
    Requiem + Kepler -> Gilgamesh, scale any scale no higher than 6 and Thomas
    Thomas effect add Kepler
    Gilgamesh effect destroy Thomas & return a contract
    Scale Kepler, Pendulum Thomas & Requiem
    XYZ / Requiem + Thomas -> Kali Yuga
    Gilgamesh -> Machinex
    """
    return True


def line_X(hand: list, main_deck: list, extra_deck: list,
           local_database: dict) -> bool:
    """
    Starting Hand:
        x.

    Searched Cards:
        x.

    Dumped Cards:
        x.

    Extra Deck Monsters:
        x.

    Combo Line:
        1.

    LINE 1 (Gilgamesh gains Requiem eff):
    Normal Kepler add Gate, Gate search Vice Requiem
    Scale Requiem, Requiem effect targeting Gate
    Requiem + Kepler -> Gilgamesh, scale any scale no higher than 6 and Thomas
    Thomas effect add Kepler
    Gilgamesh effect destroy Thomas & return a contract
    Scale Kepler, Pendulum Thomas & Requiem
    (OPTIONAL: Thomas effect special Ragnarok)
    XYZ / Requiem + Thomas -> Kali Yuga
    """
    return True


def line_X(hand: list, main_deck: list, extra_deck: list,
           local_database: dict) -> bool:
    """
    Starting Hand:
        x.

    Searched Cards:
        x.

    Dumped Cards:
        x.

    Extra Deck Monsters:
        x.

    Combo Line:
        1.

    LINE 1 (Gilgamesh gains Requiem eff):
    Normal Kepler add Gate, Gate search Vice Requiem
    Scale Requiem, Requiem effect targeting Gate
    Requiem + Kepler -> Gilgamesh, scale any scale no higher than 6 and Thomas
    Thomas effect add Kepler
    Gilgamesh effect destroy Thomas & return a contract
    Scale Kepler, Pendulum Thomas & Requiem
    (OPTIONAL: Thomas effect special Ragnarok)
    XYZ / Requiem + Thomas -> Kali Yuga
    Ragnarok -> Machinex
    """
    return True


def line_X(hand: list, main_deck: list, extra_deck: list,
           local_database: dict) -> bool:
    """
    Starting Hand:
        x.

    Searched Cards:
        x.

    Dumped Cards:
        x.

    Extra Deck Monsters:
        x.

    Combo Line:
        1.

    LINE 1 (Gilgamesh gains Requiem eff):
    Normal Kepler add Gate, Gate search Vice Requiem
    Scale Requiem, Requiem effect targeting Gate
    Requiem + Kepler -> Gilgamesh, scale any scale no higher than 6 and Thomas
    Thomas effect add Kepler
    Gilgamesh effect destroy Thomas & return a contract
    Scale Kepler, Pendulum Thomas & Requiem (OPTIONAL: Thomas effect special Ragnarok)
    XYZ / Requiem + Thomas -> Kali Yuga
    (OPTIONAL: Gilgamesh -> Machinex / Ragnarok -> Machinex)
    """
    return True


def all_one_card_combos() -> Combo:
    combos: Combo = Combo("One Card Combos")
    starting_hand: list = [
        ["D/D Savant Kepler"]
    ]
    combos.add_combo_line(ComboLine(line_1, starting_hand))
    combos.add_combo_line(ComboLine(line_2, starting_hand))
    combos.add_combo_line(ComboLine(line_3, starting_hand))
    combos.add_combo_line(ComboLine(line_4, starting_hand))
    starting_hand: list = [
        ["Dark Contract with the Gate"]
    ]
    return combos
