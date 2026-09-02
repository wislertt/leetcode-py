from collections import Counter


class Solution:
    # Time: O(n)
    # Space: O(1)
    def original_digits(self, s: str) -> str:
        counts: list[int] = [0] * 10
        c = Counter(s)
        # digits identified by a letter unique to their English word
        counts[0] = c["z"]
        counts[2] = c["w"]
        counts[4] = c["u"]
        counts[6] = c["x"]
        counts[8] = c["g"]
        # remaining digits by subtraction
        counts[1] = c["o"] - counts[0] - counts[2] - counts[4]
        counts[3] = c["h"] - counts[8]
        counts[5] = c["f"] - counts[4]
        counts[7] = c["s"] - counts[6]
        counts[9] = c["i"] - counts[5] - counts[6] - counts[8]
        return "".join(str(digit) * counts[digit] for digit in range(10))
