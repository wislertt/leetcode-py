from collections import Counter


class Solution:
    # Time: O(n)
    # Space: O(1)
    def get_hint(self, secret: str, guess: str) -> str:
        bulls = 0
        diff_secret: list[int] = []
        diff_guess: list[int] = []
        for s_digit, g_digit in zip(secret, guess, strict=True):
            if s_digit == g_digit:
                bulls += 1
            else:
                diff_secret.append(int(s_digit))
                diff_guess.append(int(g_digit))
        cows = sum((Counter(diff_secret) & Counter(diff_guess)).values())
        return f"{bulls}A{cows}B"
