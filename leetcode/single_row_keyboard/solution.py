class Solution:
    # Time: O(n + 26)
    # Space: O(26)
    def calculate_time(self, keyboard: str, word: str) -> int:
        pos = {char: i for i, char in enumerate(keyboard)}
        total = current = 0
        for char in word:
            target = pos[char]
            total += abs(target - current)
            current = target
        return total
