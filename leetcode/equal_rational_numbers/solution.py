from fractions import Fraction


class Solution:
    # Time: O(len(s) + len(t))
    # Space: O(1)
    def is_rational_equal(self, s: str, t: str) -> bool:
        return self._to_fraction(s) == self._to_fraction(t)

    def _to_fraction(self, s: str) -> Fraction:
        base, repeating = s.split("(", 1) if "(" in s else (s, "")
        repeating = repeating.rstrip(")")
        integer_part, non_repeating = base.split(".", 1) if "." in base else (base, "")
        value = Fraction(int(integer_part))
        if non_repeating:
            value += Fraction(int(non_repeating), 10 ** len(non_repeating))
        if repeating:
            scale = 10 ** len(non_repeating)
            value += Fraction(int(repeating), scale * (10 ** len(repeating) - 1))
        return value
