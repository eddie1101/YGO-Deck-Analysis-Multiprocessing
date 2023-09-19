"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503
"""

import copy
import random

from multiprocessing import Process, Value

from src.YuGiOh.ComboCategory import ComboCategory


class Deck:
    def __init__(self):
        self.main_deck: list = []
        self.extra_deck: list = []
        self.side_deck: list = []
        self.combo_categories: list[ComboCategory] = []
        self.combo_in_hand_count: int = 0
        self.full_combo_count: int = 0
        pass

    def get_main_deck(self) -> list:
        return self.main_deck

    def add_card_to_main_deck(self, card: str) -> None:
        self.main_deck.append(card)
        return None

    def get_extra_deck(self) -> list:
        return self.extra_deck

    def add_card_to_extra_deck(self, card: str) -> None:
        self.extra_deck.append(card)
        return None

    def get_side_deck(self) -> list:
        return self.side_deck

    def add_card_to_side_deck(self, card: str) -> None:
        self.side_deck.append(card)
        return None

    def print_deck(self) -> None:
        header: str = " Main Deck "
        self.print_helper(header, self.main_deck)
        header: str = " Extra Deck "
        self.print_helper(header, self.extra_deck)
        # header: str = " Side Deck "
        # self.print_helper(header, self.side_deck)
        return None

    @staticmethod
    def print_helper(header: str, deck_type: list) -> None:
        print(f'{header:~^79}')
        copies: int = 0
        curr_card: str = ""
        for card in deck_type:
            if curr_card != card:
                if curr_card != "":
                    print(f"{copies}x {curr_card}")
                    pass
                copies: int = 0
                curr_card: str = card
                pass
            copies += 1
            pass
        print(f"{copies}x {curr_card}")
        return None

    def get_combo_categories(self) -> list[ComboCategory]:
        return self.combo_categories

    def add_combo_category(self, combo_category: ComboCategory) -> None:
        self.combo_categories.append(combo_category)
        return None

    def get_combo_in_hand_count(self) -> int:
        return self.combo_in_hand_count

    def combo_in_hand(self) -> None:
        self.combo_in_hand_count += 1
        return None

    def get_full_combo_count(self) -> int:
        return self.full_combo_count

    def full_combo(self) -> None:
        self.full_combo_count += 1
        return None
    
    def analyze(self, n: int, local_database: dict) -> None:
        main_deck_src = copy.deepcopy(self.main_deck)
        for i in range(n):
            random.shuffle(main_deck_src)
            hand: list = main_deck_src[:5]
            main_deck: list = main_deck_src[5:]
            cih_lst: list[bool] = []
            fc_lst: list[bool] = []
            for combo_category in self.combo_categories:
                cih_cc, fc_cc = combo_category.test_hand(hand, main_deck,
                                                         self.extra_deck,
                                                         local_database)
                cih_lst.append(cih_cc)
                fc_lst.append(fc_cc)
                pass
            cih: bool = any(cih_lst)
            fc: bool = any(fc_lst)
            if cih:
                self.combo_in_hand_count += 1
                if fc:
                    self.full_combo_count += 1
                    pass
                pass
            pass
        return None

    def analyze_multi(self, n: int, num_threads: int, local_database: dict) -> None:
        cih_count = Value('i', 0)
        fc_count = Value('i', 0)

        processes = [Process(target=self.analyze_part, args=(int(n / num_threads), local_database, copy.deepcopy(self.main_deck), cih_count, fc_count)) for x in range(num_threads)]

        for p in processes:
            p.start()

        for p in processes:
            p.join()

        self.combo_in_hand_count = cih_count.value
        self.full_combo_count = fc_count.value

        return None
        
    
    def analyze_part(self, n: int, local_database: dict, main_deck_src: list, cih_count: Value, fc_count: Value) -> None:
        for i in range(n):
            random.shuffle(main_deck_src)
            hand: list = main_deck_src[:5]
            main_deck: list = main_deck_src[5:]
            cih_lst: list[bool] = []
            fc_lst: list[bool] = []
            for combo_category in self.combo_categories:
                cih_cc, fc_cc = combo_category.test_hand(hand, main_deck,
                                                         self.extra_deck,
                                                         local_database)
                cih_lst.append(cih_cc)
                fc_lst.append(fc_cc)
                pass
            cih: bool = any(cih_lst)
            fc: bool = any(fc_lst)
            if cih:
                with cih_count.get_lock():
                    cih_count.value += 1
                if fc:
                    with fc_count.get_lock():
                        fc_count.value += 1
                    pass
                pass
            pass
        return None

    def print_analysis(self, n: int, analysis_level: int = 3,
                       detailed: bool = False) -> None:
        if detailed:
            print(f"[A/B/C]\n"
                  f"A: Probability of executing FC\n"
                  f"B: Probability of opening FC\n"
                  f"C: Probability of executing FC if opened FC\n")
            pass
        for category in self.get_combo_categories():
            category.print_analysis(n, analysis_level)
            pass
        pass

    pass
