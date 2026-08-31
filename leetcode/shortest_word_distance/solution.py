class Solution:
    # Time: O(n)
    # Space: O(1)
    def shortest_distance(self, words_dict: list[str], word1: str, word2: str) -> int:
        index1 = -1
        index2 = -1
        shortest = len(words_dict)
        for i, word in enumerate(words_dict):
            if word == word1:
                index1 = i
            if word == word2:
                index2 = i
            if index1 != -1 and index2 != -1:
                shortest = min(shortest, abs(index1 - index2))
        return shortest
