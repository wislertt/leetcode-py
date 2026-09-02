class Solution:
    # Time: O(n)
    # Space: O(1)
    def detect_capital_use(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
