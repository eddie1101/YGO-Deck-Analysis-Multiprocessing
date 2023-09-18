"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503
"""

from src.YuGiOh.Combo import Combo


class ComboCategory:
    def __init__(self, combo_category: str):
        self.combo_category: str = combo_category
        self.combos: list[Combo] = []
        self.combo_in_hand_count: int = 0
        self.full_combo_count: int = 0
        pass

    def get_combo_category(self) -> str:
        return self.combo_category

    def get_combos(self) -> list[Combo]:
        return self.combos

    def add_combo(self, combo: any) -> None:
        self.combos.append(combo)
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

    def test_hand(self, hand: list, main_deck: list, extra_deck: list,
                  local_database: dict) -> tuple[bool, bool]:
        cih_lst: list[bool] = []
        fc_lst: list[bool] = []
        for combo in self.combos:
            cih_c, fc_c = combo.test_hand(hand, main_deck, extra_deck,
                                          local_database)
            cih_lst.append(cih_c)
            fc_lst.append(fc_c)
            pass
        cih: bool = any(cih_lst)
        fc: bool = any(fc_lst)
        if cih:
            self.combo_in_hand_count += 1
            if fc:
                self.full_combo_count += 1
                pass
            pass
        return cih, fc

    def print_analysis(self, n: int, detail_level: int) -> None:
        p_a: float = self.full_combo_count / n
        p_b: float = self.combo_in_hand_count / n
        p_c: float = p_a / p_b
        print(f"{self.combo_category}: "
              f"[{100 * p_a:.4f}% / {100 * p_b:.4f}% / {100 * p_c:.4f}%]")
        if detail_level > 1:
            for combo in self.combos:
                combo.print_analysis(n, detail_level)
                pass
            pass
        return None

    pass
