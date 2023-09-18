"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503
"""
import copy

from src.YuGiOh.ComboLine import ComboLine


class Combo:
    def __init__(self, combo_description: str):
        self.combo_description: str = combo_description
        self.combo_lines: list[ComboLine] = []
        self.combo_in_hand_count: int = 0
        self.full_combo_count: int = 0
        pass

    def get_combo_description(self) -> str:
        return self.combo_description

    def get_combo_lines(self) -> list[ComboLine]:
        return self.combo_lines

    def add_combo_line(self, combo_line: ComboLine) -> None:
        self.combo_lines.append(combo_line)
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
        for combo_line in self.combo_lines:
            cih_cl, fc_cl = combo_line.test_hand(copy.deepcopy(hand),
                                                 copy.deepcopy(main_deck),
                                                 copy.deepcopy(extra_deck),
                                                 local_database)
            cih_lst.append(cih_cl)
            fc_lst.append(fc_cl)
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
        print(f"\t{self.combo_description}: "
              f"[{100 * p_a:.4f}% / {100 * p_b:.4f}% / {100 * p_c:.4f}%]")
        if detail_level > 2:
            for i, combo_line in enumerate(self.combo_lines):
                combo_line.print_analysis(n, i + 1)
                pass
            pass
        return None

    pass
