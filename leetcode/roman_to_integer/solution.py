class Solution:
    # Time: O(n)
    # Space: O(1)
    def roman_to_int(self, s: str) -> int:
        values: dict[str, int] = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0
        prev = 0
        # Walk right-to-left; subtract when a symbol is smaller than the previous one
        for char in reversed(s):
            current = values[char]
            if current < prev:
                total -= current
            else:
                total += current
            prev = current

        return total
