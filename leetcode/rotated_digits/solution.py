class Solution:
    # Time: O(log n)
    # Space: O(log n)
    def rotated_digits(self, n: int) -> int:
        valid = frozenset("0125689")
        flipping = frozenset("2569")
        digits = str(n)
        total = 0
        has_flip = False
        for i, ch in enumerate(digits):
            rest = len(digits) - i - 1
            for c in "0123456789"[: int(ch)]:
                if c not in valid:
                    continue
                if has_flip or c in flipping:
                    total += 7**rest
                else:
                    total += 7**rest - 3**rest
            if ch not in valid:
                return total
            has_flip = has_flip or ch in flipping
        return total + (1 if has_flip else 0)
