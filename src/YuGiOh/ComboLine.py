"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503
"""

from multiprocessing import Value

class ComboLine:
    def __init__(self, func: any, starting_hands: list):
        self.func: any = func
        self.starting_hands: list = starting_hands
        self.combo_in_hand_count: Value = Value("i", 0)
        self.full_combo_count: Value = Value("i", 0)
        pass

    def get_starting_hands(self) -> list:
        return self.starting_hands

    def get_combo_in_hand_count(self) -> int:
        return self.combo_in_hand_count.value

    def combo_in_hand(self) -> None:
        with self.combo_in_hand_count.get_lock():
            self.combo_in_hand_count.value += 1
        return None

    def is_combo_in_hand(self, hand: list) -> bool:
        for starting_hand in self.starting_hands:
            if all(card in hand for card in starting_hand):
                with self.combo_in_hand_count.get_lock():
                    self.combo_in_hand_count.value += 1
                return True
            pass
        return False

    def get_full_combo_count(self) -> int:
        return self.full_combo_count.value

    def full_combo(self) -> None:
        with self.full_combo_count.get_lock():
            self.full_combo_count.value += 1
        return None

    def is_full_combo(self, hand: list, main_deck: list, extra_deck: list,
                      local_database: dict) -> bool:
        full_combo: bool = self.func(hand, main_deck, extra_deck,
                                     local_database)
        if full_combo:
            with self.full_combo_count.get_lock():
                self.full_combo_count.value += 1
            pass
        return full_combo

    def test_hand(self, hand: list, main_deck: list, extra_deck: list,
                  local_database: dict) -> tuple[bool, bool]:
        # print(hand)
        cih: bool = self.is_combo_in_hand(hand)
        fc: bool = self.is_full_combo(hand, main_deck, extra_deck,
                                      local_database) if cih else False
        # if (cih) and (not fc):
        #     print(hand)
        #     pass
        # print("")
        return cih, fc

    def print_analysis(self, n: int, combo_line_num: int) -> None:
        p_a: float = self.full_combo_count.value / n
        p_b: float = self.combo_in_hand_count.value / n
        p_c: float = p_a / p_b
        print(f"\t\tCombo Line {combo_line_num}: "
              f"[{100 * p_a:.4f}% / {100 * p_b:.4f}% / {100 * p_c:.4f}%]")
        return None

    pass
