class Solution:
    # Time: O(n)
    # Space: O(1)
    def is_circular_sentence(self, sentence: str) -> bool:
        for i, char in enumerate(sentence):
            if char == " " and sentence[i - 1] != sentence[i + 1]:
                return False
        return sentence[0] == sentence[-1]
