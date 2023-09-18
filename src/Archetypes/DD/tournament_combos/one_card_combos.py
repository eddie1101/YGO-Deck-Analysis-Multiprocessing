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
        4. LS Gilgamesh [Kepler + Gryphon]; Scale (0 Scale + D/D Cerberus)
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
    search: str = "Dark Contract with the Gate"
    if not utils_dd.kepler_search(search, hand, main_deck):
        if not utils.soft_brick_in_hand(search, hand):
            return False
        pass
    search: str = "D/D Gryphon"
    if not utils_dd.gate_search(search, hand, main_deck):
        if not utils.soft_brick_in_hand(search, hand):
            return False
        pass
    ed_monster: str = "D/D/D Abyss King Gilgamesh"
    if not utils.extra_deck_summon(ed_monster, extra_deck):
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
    extra_deck_monsters: list = [
        "D/D/D Wave King Caesar",
        "D/D/D Marksman King Tell",
        "D/D/D Abyss King Gilgamesh"
    ]
    for extra_deck_monster in extra_deck_monsters:
        if not utils.extra_deck_summon(extra_deck_monster, extra_deck):
            return False
        pass
    dump: str = "D/D Necro Slime"
    if not utils.dump_card_from_deck_to_GY(dump, main_deck):
        if not utils.soft_brick_in_hand(dump, hand):
            return False
        pass
    extra_deck_monsters: list = [
        "D/D/D Flame King Genghis",
        "D/D/D Deviser King Deus Machinex",
        "D/D/D Abyss King Gilgamesh"
    ]
    for extra_deck_monster in extra_deck_monsters:
        if not utils.extra_deck_summon(extra_deck_monster, extra_deck):
            return False
        pass
    search: str = "Dark Contract with the Swamp King"
    if not utils.dump_card_from_deck_to_GY(search, main_deck):
        if not utils.soft_brick_in_hand(dump, hand):
            return False
        pass
    extra_deck_monsters: list = [
        "D/D/D Flame King Genghis",
        "D/D/D Wave High King Caesar",
        "D/D/D Deviser King Deus Machinex"
    ]
    for extra_deck_monster in extra_deck_monsters:
        if not utils.extra_deck_summon(extra_deck_monster, extra_deck):
            return False
        pass
    return True


def all_one_card_combos() -> Combo:
    combos: Combo = Combo("One Card Combos")
    starting_hand: list = [
        ["D/D Savant Kepler"]
    ]
    combos.add_combo_line(ComboLine(line_1, starting_hand))
    return combos
